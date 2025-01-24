from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionConfirm(Action):
    def name(self) -> Text:
        return "action_confirm"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Apakah informasi tersebut sesuai dengan yang Sobat cari?"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "ya",
                                "title": "Ya"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "tidak",
                                "title": "Tidak"
                            }
                        },
                    ]
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(attachment=message)
        return []

