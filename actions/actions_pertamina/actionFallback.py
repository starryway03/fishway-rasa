from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        agent = {
            "type": "is_fallback",
            "message": "Mohon maaf, SIERA belum mengerti apa yang Sobat maksud."
        }

        dispatcher.utter_message(attachment=agent)
        return []

