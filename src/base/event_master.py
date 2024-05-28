from typing import Callable, List

class EventNode:
    def __init__(self, subject: str, trigger: Callable):
        self.subject = subject
        self.trigger = trigger
        self.observer: List[str] = []


class EventMaster:
    def __init__(self):
        self._event_list: List[EventNode] = []
    
    def _get_event_node(self, subject: str):
        for node in self._event_list:
            if node.subject == subject:
                return node
        raise ValueError('subject[%s] is not in event list' % subject)

    def set_observer(self, observer: str, subject: str, callback: Callable, args: List):
        event_node = self._get_event_node(subject)
        event_node.trigger(lambda: callback(*args))
        event_node.observer.append(observer)

    def delete_observer(self, observer: str, subject: str):
        event_node = self._get_event_node(subject)
        event_node.observer.remove(observer)

    def set_subject(self, subject: str, trigger: Callable):
        event_node = EventNode(subject, trigger)
        self._event_list.append(event_node)