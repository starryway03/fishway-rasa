from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionHelp(Action):
    def name(self) -> Text:
        return "action_help"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Apa yang bisa SIERA bantu? Silahkan Sobat pilih dari menu berikut ini."
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "faq",
                                "title": "FAQ"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "CekTiket",
                                "title": "Cek Tiket"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "ChatAgent",
                                "title": "Chat dengan Agent"
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

