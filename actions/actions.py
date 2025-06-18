from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionExtractSlots(Action):
    def name(self) -> Text:
        return "action_extract_slots"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get("entities", [])
        dispatcher.utter_message(text=f"Extracted entities: {entities}")
        return []
