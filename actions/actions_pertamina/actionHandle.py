from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHandle(Action):
    def name(self) -> Text:
        return "action_handle"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ticket_id = tracker.get_slot('ticket')

        if ticket_id == 'MOB0000002420001':
            dispatcher.utter_message(text = "Update status tiketmu MOB0000002420001 sebagai berikut:\nStatus: In Progress\nDescription:\nReason:\nSLA:")
        elif ticket_id == 'MOB0000002420002':
            dispatcher.utter_message(text = "Update status tiketmu MOB0000002420002 sebagai berikut:\nStatus: In Progress\nDescription:\nReason:\nSLA:")
        elif ticket_id == 'MOB0000002420003':
            dispatcher.utter_message(text = "Update status tiketmu MOB0000002420003 sebagai berikut:\nStatus: In Progress\nDescription:\nReason:\nSLA:")
        elif ticket_id == 'MOB0000002420004':
            dispatcher.utter_message(text = "Update status tiketmu MOB0000002420004 sebagai berikut:\nStatus: In Progress\nDescription:\nReason:\nSLA:")
        else:
            dispatcher.utter_message(text = "Update status tiketmu MOB0000002420005 sebagai berikut:\nStatus: In Progress\nDescription:\nReason:\nSLA:")

        return []
