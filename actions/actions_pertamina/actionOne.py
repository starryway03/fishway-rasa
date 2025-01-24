from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionOne(Action):
    def name(self) -> Text:
        return "action_one"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Silahkan Sobat pilih layanan dari menu berikut ini:"
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Pilihan:",
                            "rows": [
                                {
                                    "id": "AccountAccess",
                                    "title": "Account and Access",  # 18 chara
                                    "description": "Layanan Account and Access",  # 26 chara
                                },
                                {
                                    "id": "ApplicationSoftware",
                                    "title": "Application and Software",  # 24 chara
                                    "description": "Layanan Application and Software",  # 32 chara
                                },
                                {
                                    "id": "NetworkVoiceConnectivity",
                                    "title": "Network, Voice & Connect",  # 24 chara
                                    "description": "Layanan Network, Voice and Connectivity",  # 39 chara
                                }
                            ],
                        },
                    ],
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(text="Berikut layanan yang tersedia pada Tower ICT yang bisa Sobat pilih.")
        dispatcher.utter_message(attachment=message)
        return []
