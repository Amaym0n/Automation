import json
from typing import Any, Optional

import allure
from jsonschema.validators import validator_for, RefResolver


class SchemaConstruct:
    """ Конструктор json схем """
    def __init__(self, base_schema: dict[str, Any], definitions_schema: Optional[dict[str, Any]] = None) -> None:
        self.base_schema = base_schema
        self.schema_resolver = self._schema_resolver(definitions_schema=definitions_schema) if definitions_schema \
            else None

    def _schema_resolver(self, definitions_schema: dict[str, Any]) -> RefResolver:
        """ Конструктор схемы """
        schema_store = {self.base_schema.get('$id', 'base.schema.json'): self.base_schema}
        schema_store.update({definitions_schema.get('$id', 'definitions.schema.json'): definitions_schema})
        return RefResolver.from_schema(self.base_schema, store=schema_store)

    def validation(self, response: bytes) -> None:
        """ Валидатор переданной схемы """
        with allure.step('Валидация json схемы'):
            validator = validator_for(schema=True)(schema=True, resolver=None)
            validator.validate(json.loads(response), self.base_schema)
