from aiohttp import web
from aiohttp_jinja2 import template
from sqlalchemy.exc import NoResultFound

from .models import Post, User


class HomeView(web.View):
    @template("home.html")
    async def get(self):
        all_posts = await Post.all()
        print(all_posts)
        username = self.request.user.username if self.request.user else "Anonymous"

        # Возвращаем контекст в шаблон.
        return {"title": "Hello World", "user": username, "posts": all_posts}


class NoteCreateView(web.View):
    @template("notes/create_form.html")
    async def get(self):
        return {}

    @template("notes/create_form.html")
    async def post(self):
        user_data = await self.request.post()
        title = user_data.get('title')
        content = user_data.get('content')
        post = await Post.create(title=title, content=content, user_id=self.request.user)
        print(post)

        raise web.HTTPFound("/")
        # raise web.HTTPFound(f"/notes/{post.id}")
        
class NoteDeleteView(web.View):
    @template("notes/update.html")
    async def post(self):
        if not self.request.user:
            raise web.HTTPForbidden()
        
        post_id = int(self.request.match_info.get('post_id', -1))
        post: Post = await Post.get(post_id=post_id)
        if post.user_id != self.request.user.id:
            raise web.HTTPForbidden()
        if post:
            await post.delete()
            return web.HTTPFound("/")
        else:
            return web.HTTPNotFound()
        # deleted_post = await Post.delete(post_id=post_id)
        # if deleted_post:
        #     raise web.HTTPFound(f'/')
        # else:
        #     return {"post": deleted_post, "error": "не удалось удалить заметку"}


class NoteUpdateView(web.View):
    @template("notes/update.html")
    async def get(self):
        if not self.request.user:
            raise web.HTTPForbidden()
        #post_id = int(self.request.match_info.get('post_id', -1))
        post: Post = await Post.get(id=self.request.match_info.get('post_id'))
        if post.user_id != self.request.user.id:
            raise web.HTTPForbidden()
        #post = await Post.get_by_id(post_id)
        return {"post": post}

    @template("notes/update.html")
    async def post(self):
        post_id = int(self.request.match_info.get('post_id', -1))
        post_data = await self.request.post()
        action = post_data.get('action')
        post = None

        if post_id != -1:
            title = post_data.get('title', '')
            content = post_data.get('content', '')
            user_id = int(post_data.get('user_id', -1))
            updated_post = await Post.update(post_id=post_id, title=title, content=content, user_id=user_id)
            if updated_post:
                raise web.HTTPFound(f"/")
            else:
                post = await Post.get_by_id(post_id)
            if not post:
                post = await Post.get_by_id(post_id)
            return {"post": post, "error": "Не удалось обновить заметку."}
        else:
            raise web.HTTPFound(f"/")


class LoginView(web.View):

    @template("account/login.html")
    async def get(self):
        return {}  # Нет контекста.

    @template("account/login.html")
    async def post(self):
        user_data = await self.request.post()

        username = user_data.get('username')
        password = user_data.get('password')

        try:
            user = await User.get_valid_user(username, password)
        except NoResultFound:
            return {"error": "Invalid username or password"}

        # Создать сессию пользователя!
        self.request.session["user_id"] = user.id

        raise web.HTTPFound("/")  # Перенаправление на главную!
    
class RegisterView(web.View):
    @template("account/register.html")
    async def get(self):
        return {}

    @template("account/register.html")
    async def post(self):
        user_data = await self.request.post()
        username = user_data.get('username')
        password = user_data.get('password')
        email = user_data.get('email')
        password_confirm = user_data.get('password_confirm')
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        middle_name = user_data.get('middle_name')

        if await User.get_existing_user(user_data.get("username")):
            return {"error": "username already taken"}

        if password != password_confirm:
            return {"error": "passwords don't match"}

        try:
            user = await User.create_user(username=username, email=email, password=password,first_name=first_name,last_name=last_name,middle_name=middle_name)

            return web.HTTPFound("/login")
        except sqlalchemy.exc.SQLAlchemyError as e:
            return {"error": "Database error"}