from typing import Any, Text, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateTicketForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_ticket_form"

    def validate_ticket(self,
                        slot_value: Any, dispatcher: CollectingDispatcher,
                        tracker: Tracker, domain: DomainDict,
                        ) -> Dict[Text, Any]:

        if re.match(r"MOB000000242000\d", slot_value):
            return {"ticket": slot_value}

        else:
            dispatcher.utter_message(text="Mohon maaf, silahkan pilih status update salah satu tiket.")
            return {"ticket": None}
