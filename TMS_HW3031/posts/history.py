from django.core.handlers.wsgi import WSGIRequest

import uuid

from .models import Note

class HistoryPageNotes:
    
    def __init__(self, request: WSGIRequest):
        self._session = request.session
        
        self._session.setdefault("history", [])
    
        if not isinstance(self._session["history"], list):
                self._session["history"] = [] 
    
    
    
    def add_page(self, note: Note) -> None:
        
        # self._session["history"].append(str(note.uuid))
        # self._session.save()
        
        if len(self._session["history"]) >= 20:
            self._session["history"].pop(0)
            self._session["history"].append(str(note.uuid))
        elif str(note.uuid) in self._session["history"]:
            self._session["history"].remove(str(note.uuid))
            self._session["history"].append(str(note.uuid))                
        else :     
            self._session["history"].append(str(note.uuid))
        self._session.save()
    
    @property
    def history_uuids(self) -> list[str]:
        return self._session["history"]
    
def history_service_preprocessor(request: WSGIRequest) -> dict[str, list[str]]:
    return {"history_uuids": HistoryPageNotes(request).history_uuids}

