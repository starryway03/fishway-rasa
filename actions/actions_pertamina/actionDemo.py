from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionDemo(Action):
    def name(self) -> Text:
        return "action_demo"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Silahkan pencet tombol di bawah ini untuk kembali ke menu utama:"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "MenuUtama",
                                "title": "Menu Utama"
                            }
                        },
                    ]
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(text="Maaf, sepertinya layanan yang ingin kamu pilih belum tersedia untuk saat ini.")
        dispatcher.utter_message(attachment=message)
        return []
