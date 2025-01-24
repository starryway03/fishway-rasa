from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionApp(Action):
    def name(self) -> Text:
        return "action_app"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message = {
            "interactive": {
                "type": "list",
                "body": {
                    "text": "Silahkan Sobat pilih informasi tentang Application and Software dari menu berikut ini:"
                },
                "action": {
                    "button": "Menu",
                    "sections": [
                        {
                            "title": "Pilihan:",
                            "rows": [
                                {
                                    "id": "NonERP",
                                    "title": "Non ERP",  # 7 chara
                                    "description": "Info tentang Non ERP",  # 20 chara
                                }
                            ],
                        },
                    ],
                }
                # end action
            }
            # end interactive
        }
        dispatcher.utter_message(text="Berikut informasi tentang Application and Software yang bisa Sobat pilih.")
        dispatcher.utter_message(attachment=message)
        return []
