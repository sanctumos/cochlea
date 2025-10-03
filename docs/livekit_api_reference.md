# LiveKit SDK API Reference

*Generated from installed LiveKit SDK packages*
*Total modules documented: 12*

---

## Table of Contents

- [livekit](#livekit)
- [livekit.agents](#livekit-agents)
- [livekit.agents.llm](#livekit-agents-llm)
- [livekit.agents.stt](#livekit-agents-stt)
- [livekit.agents.tts](#livekit-agents-tts)
- [livekit.api](#livekit-api)
- [livekit.plugins](#livekit-plugins)
- [livekit.plugins.cartesia](#livekit-plugins-cartesia)
- [livekit.plugins.deepgram](#livekit-plugins-deepgram)
- [livekit.plugins.openai](#livekit-plugins-openai)
- [livekit.plugins.silero](#livekit-plugins-silero)
- [livekit.protocol](#livekit-protocol)

---

## livekit {#livekit}

**Description:** No documentation available

### Examples

```python
# Import livekit
import livekit
```

---

## livekit.agents {#livekit-agents}

**Description:** LiveKit Agents for Python

See [https://docs.livekit.io/agents/](https://docs.livekit.io/agents/) for quickstarts,
documentation, and examples.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\agents\__init__.py`

### Classes

#### APIConnectOptions

APIConnectOptions(max_retry: int = 3, retry_interval: float = 2.0, timeout: float = 10.0)

**Inherits from:** object


#### APIConnectionError

Raised when an API request failed due to a connection error.

**Inherits from:** APIError


#### APIError

Raised when an API request failed.
This is used on our TTS/STT/LLM plugins.

**Inherits from:** Exception


#### APIStatusError

Raised when an API response has a status code of 4xx or 5xx.

**Inherits from:** APIError


#### APITimeoutError

Raised when an API request timed out.

**Inherits from:** APIConnectionError


#### Agent

No documentation available

**Inherits from:** object


#### AgentSession

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

    class Mapping[KT, VT]:
        def __getitem__(self, key: KT) -> VT:
            ...
        # Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

    def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
        try:
            return mapping[key]
        except KeyError:
            return default

**Inherits from:** EventEmitter, Generic


#### AgentStateChangedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### AssignmentTimeoutError

Raised when accepting a job but not receiving an assignment within the specified timeout.
The server may have chosen another worker to handle this job.

**Inherits from:** Exception


#### AudioConfig

Definition for the audio to be played in the background

Args:
    volume: The volume of the audio (0.0-1.0)
    probability: The probability of the audio being played, when multiple
        AudioConfigs are provided (0.0-1.0)

**Inherits from:** tuple


#### AutoSubscribe

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.

**Inherits from:** str, Enum


#### BackgroundAudioPlayer

No documentation available

**Inherits from:** object


#### BuiltinAudioClip

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

**Inherits from:** Enum


#### ChatContext

No documentation available

**Inherits from:** object

**Methods:**

- `empty() -> 'ChatContext'`
 - No documentation available...

- `from_dict(data: 'dict[str, Any]') -> 'ChatContext'`
 - No documentation available...


#### ChatMessage

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### CloseEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### ConversationItemAddedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### ErrorEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FunctionCall

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FunctionCallOutput

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FunctionTool

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...

**Inherits from:** Protocol


#### JobContext

No documentation available

**Inherits from:** object


#### JobExecutorType

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

**Inherits from:** Enum


#### JobProcess

No documentation available

**Inherits from:** object


#### JobRequest

No documentation available

**Inherits from:** object


#### MetricsCollectedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### ModelSettings

ModelSettings(tool_choice: 'NotGivenOr[llm.ToolChoice]' = NOT_GIVEN)

**Inherits from:** object


#### NotGiven

No documentation available

**Inherits from:** object


#### Plugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### RoomIO

No documentation available

**Inherits from:** object


#### RoomInputOptions

RoomInputOptions(text_enabled: 'NotGivenOr[bool]' = NOT_GIVEN, audio_enabled: 'NotGivenOr[bool]' = NOT_GIVEN, video_enabled: 'NotGivenOr[bool]' = NOT_GIVEN, audio_sample_rate: 'int' = 24000, audio_num_channels: 'int' = 1, noise_cancellation: 'rtc.NoiseCancellationOptions | None' = None, text_input_cb: 'TextInputCallback' = <function _default_text_input_cb at 0x00000192A8171F80>, participant_kinds: 'NotGivenOr[list[rtc.ParticipantKind.ValueType]]' = NOT_GIVEN, participant_identity: 'NotGivenOr[str]' = NOT_GIVEN, pre_connect_audio: 'bool' = True, pre_connect_audio_timeout: 'float' = 3.0, close_on_disconnect: 'bool' = True)

**Inherits from:** object


#### RoomOutputOptions

RoomOutputOptions(transcription_enabled: 'NotGivenOr[bool]' = NOT_GIVEN, audio_enabled: 'NotGivenOr[bool]' = NOT_GIVEN, audio_sample_rate: 'int' = 24000, audio_num_channels: 'int' = 1, audio_publish_options: 'rtc.TrackPublishOptions' = <factory>, sync_transcription: 'NotGivenOr[bool]' = NOT_GIVEN)

**Inherits from:** object


#### RunContext

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

    class Mapping[KT, VT]:
        def __getitem__(self, key: KT) -> VT:
            ...
        # Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

    def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
        try:
            return mapping[key]
        except KeyError:
            return default

**Inherits from:** Generic


#### SimulateJobInfo

SimulateJobInfo(room: 'str', participant_identity: 'str | None' = None)

**Inherits from:** object


#### SpeechCreatedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### StopResponse

Common base class for all non-exit exceptions.

**Inherits from:** Exception


#### ToolError

Common base class for all non-exit exceptions.

**Inherits from:** Exception


#### UserInputTranscribedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### UserStateChangedEvent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### Worker

Abstract base class for generic types.

On Python 3.12 and newer, generic classes implicitly inherit from
Generic when they declare a parameter list after the class's name::

    class Mapping[KT, VT]:
        def __getitem__(self, key: KT) -> VT:
            ...
        # Etc.

On older versions of Python, however, generic classes have to
explicitly inherit from Generic.

After a class has been declared to be generic, it can then be used as
follows::

    def lookup_name[KT, VT](mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
        try:
            return mapping[key]
        except KeyError:
            return default

**Inherits from:** EventEmitter


#### WorkerOptions

WorkerOptions(entrypoint_fnc: 'Callable[[JobContext], Awaitable[None]]', request_fnc: 'Callable[[JobRequest], Awaitable[None]]' = <function _default_request_fnc at 0x00000192A7AB1E40>, prewarm_fnc: 'Callable[[JobProcess], Any]' = <function _default_initialize_process_fnc at 0x00000192A7834220>, load_fnc: 'Callable[[Worker], float] | Callable[[], float]' = <bound method _DefaultLoadCalc.get_load of <class 'livekit.agents.worker._DefaultLoadCalc'>>, job_executor_type: 'JobExecutorType' = <JobExecutorType.THREAD: 'thread'>, load_threshold: 'float | _WorkerEnvOption[float]' = _WorkerEnvOption(dev_default=inf, prod_default=0.75), job_memory_warn_mb: 'float' = 500, job_memory_limit_mb: 'float' = 0, drain_timeout: 'int' = 1800, num_idle_processes: 'int | _WorkerEnvOption[int]' = _WorkerEnvOption(dev_default=0, prod_default=22), shutdown_process_timeout: 'float' = 60.0, initialize_process_timeout: 'float' = 10.0, permissions: 'WorkerPermissions' = <factory>, agent_name: 'str' = '', worker_type: 'WorkerType' = <WorkerType.ROOM: 0>, max_retry: 'int' = 16, ws_url: 'str' = 'ws://localhost:7880', api_key: 'str | None' = None, api_secret: 'str | None' = None, _worker_token: 'str | None' = None, host: 'str' = '', port: 'int | _WorkerEnvOption[int]' = _WorkerEnvOption(dev_default=0, prod_default=8081), http_proxy: 'NotGivenOr[str | None]' = NOT_GIVEN, multiprocessing_context: "Literal['spawn', 'forkserver']" = 'spawn')

**Inherits from:** object

**Methods:**

- `load_fnc(worker: 'Worker') -> 'float'`
 - No documentation available...


#### WorkerPermissions

WorkerPermissions(can_publish: 'bool' = True, can_subscribe: 'bool' = True, can_publish_data: 'bool' = True, can_update_metadata: 'bool' = True, can_publish_sources: 'list[models.TrackSource]' = <factory>, hidden: 'bool' = False)

**Inherits from:** object


#### WorkerType

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

  >>> Color.RED
  <Color.RED: 1>

- value lookup:

  >>> Color(1)
  <Color.RED: 1>

- name lookup:

  >>> Color['RED']
  <Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.

**Inherits from:** Enum


### Functions

#### function_tool(f: 'F | Raw_F | None' = None, *, name: 'str | None' = None, description: 'str | None' = None, raw_schema: 'RawFunctionDescription | dict[str, Any] | None' = None) -> 'FunctionTool | RawFunctionTool | Callable[[F], FunctionTool] | Callable[[Raw_F], RawFunctionTool]'

No documentation available

**Parameters:**

- `f` (F | Raw_F | None) = None
- `name` (str | None) = None
- `description` (str | None) = None
- `raw_schema` (RawFunctionDescription | dict[str, Any] | None) = None


#### get_job_context() -> 'JobContext'

No documentation available


### Constants

- `DEFAULT_API_CONNECT_OPTIONS` = `APIConnectOptions(max_retry=3, retry_interval=2.0, timeout=10.0)`
- `NOT_GIVEN` = `NOT_GIVEN`
- `NOT_IN_ALL` = `['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__getattr__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_exceptions', 'debug', 'http_server', 'inference_runner', 'job', 'log', 'plugin', 'types', 'typing', 'version', 'worker']`
- `n` = `worker`

### Examples

```python
# Import livekit.agents
import livekit.agents
```
```python
# Using AgentStateChangedEvent
from livekit.agents import AgentStateChangedEvent


# Call construct
result = instance.construct()
```

```python
# Using ChatContext
from livekit.agents import ChatContext


# Call empty
result = instance.empty()
```

```python
# Using ChatMessage
from livekit.agents import ChatMessage


# Call construct
result = instance.construct()
```

```python
# Using CloseEvent
from livekit.agents import CloseEvent


# Call construct
result = instance.construct()
```

```python
# Using ConversationItemAddedEvent
from livekit.agents import ConversationItemAddedEvent


# Call construct
result = instance.construct()
```

```python
# Using ErrorEvent
from livekit.agents import ErrorEvent


# Call construct
result = instance.construct()
```

```python
# Using FunctionCall
from livekit.agents import FunctionCall


# Call construct
result = instance.construct()
```

```python
# Using FunctionCallOutput
from livekit.agents import FunctionCallOutput


# Call construct
result = instance.construct()
```

```python
# Using MetricsCollectedEvent
from livekit.agents import MetricsCollectedEvent


# Call construct
result = instance.construct()
```

```python
# Using Plugin
from livekit.agents import Plugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using SpeechCreatedEvent
from livekit.agents import SpeechCreatedEvent


# Call construct
result = instance.construct()
```

```python
# Using UserInputTranscribedEvent
from livekit.agents import UserInputTranscribedEvent


# Call construct
result = instance.construct()
```

```python
# Using UserStateChangedEvent
from livekit.agents import UserStateChangedEvent


# Call construct
result = instance.construct()
```

```python
# Using WorkerOptions
from livekit.agents import WorkerOptions


# Call load_fnc
result = instance.load_fnc()
```


---

## livekit.agents.llm {#livekit-agents-llm}

**Description:** No documentation available

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\agents\llm\__init__.py`

### Classes

#### AudioContent

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### AvailabilityChangedEvent

AvailabilityChangedEvent(llm: 'LLM', available: 'bool')

**Inherits from:** object


#### ChatChunk

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### ChatContext

No documentation available

**Inherits from:** object

**Methods:**

- `empty() -> 'ChatContext'`
 - No documentation available...

- `from_dict(data: 'dict[str, Any]') -> 'ChatContext'`
 - No documentation available...


#### ChatMessage

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### ChoiceDelta

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### CompletionUsage

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FallbackAdapter

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** LLM


#### FunctionCall

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FunctionCallOutput

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### FunctionTool

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...

**Inherits from:** Protocol


#### FunctionToolCall

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### GenerationCreatedEvent

GenerationCreatedEvent(message_stream: 'AsyncIterable[MessageGeneration]', function_stream: 'AsyncIterable[FunctionCall]', user_initiated: 'bool')

**Inherits from:** object


#### ImageContent

ImageContent is used to input images into the ChatContext on supported LLM providers / plugins.

You may need to consult your LLM provider's documentation on supported URL types.

```python
# Pass a VideoFrame directly, which will be automatically converted to a JPEG data URL internally
async for event in rtc.VideoStream(video_track):
    chat_image = ImageContent(image=event.frame)
    # this instance is now available for your ChatContext

# Encode your VideoFrame yourself for more control, and pass the result as a data URL (see EncodeOptions for more details)
from livekit.agents.utils.images import encode, EncodeOptions, ResizeOptions

image_bytes = encode(
    event.frame,
    EncodeOptions(
        format="PNG",
        resize_options=ResizeOptions(width=512, height=512, strategy="scale_aspect_fit"),
    ),
)
chat_image = ImageContent(
    image=f"data:image/png;base64,{base64.b64encode(image_bytes).decode('utf-8')}"
)

# With an external URL
chat_image = ImageContent(image="https://example.com/image.jpg")
```

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### InputSpeechStartedEvent

InputSpeechStartedEvent()

**Inherits from:** object


#### InputSpeechStoppedEvent

InputSpeechStoppedEvent(user_transcription_enabled: 'bool')

**Inherits from:** object


#### InputTranscriptionCompleted

InputTranscriptionCompleted(item_id: 'str', transcript: 'str', is_final: 'bool')

**Inherits from:** object


#### LLM

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC, EventEmitter, Generic


#### LLMError

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### LLMStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC


#### MessageGeneration

MessageGeneration(message_id: 'str', text_stream: 'AsyncIterable[str]', audio_stream: 'AsyncIterable[rtc.AudioFrame]')

**Inherits from:** object


#### RawFunctionTool

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto[T](Protocol):
        def meth(self) -> T:
            ...

**Inherits from:** Protocol


#### RealtimeCapabilities

RealtimeCapabilities(message_truncation: 'bool', turn_detection: 'bool', user_transcription: 'bool', auto_tool_reply_generation: 'bool')

**Inherits from:** object


#### RealtimeError

Common base class for all non-exit exceptions.

**Inherits from:** Exception


#### RealtimeModel

No documentation available

**Inherits from:** object


#### RealtimeModelError

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### RealtimeSession

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC, EventEmitter, Generic


#### RealtimeSessionReconnectedEvent

RealtimeSessionReconnectedEvent()

**Inherits from:** object


#### StopResponse

Common base class for all non-exit exceptions.

**Inherits from:** Exception


#### ToolContext

Stateless container for a set of AI functions

**Inherits from:** object

**Methods:**

- `empty() -> 'ToolContext'`
 - No documentation available...


#### ToolError

Common base class for all non-exit exceptions.

**Inherits from:** Exception


### Functions

#### find_function_tools(cls_or_obj: 'Any') -> 'list[FunctionTool | RawFunctionTool]'

No documentation available

**Parameters:**

- `cls_or_obj` (Any)


#### function_tool(f: 'F | Raw_F | None' = None, *, name: 'str | None' = None, description: 'str | None' = None, raw_schema: 'RawFunctionDescription | dict[str, Any] | None' = None) -> 'FunctionTool | RawFunctionTool | Callable[[F], FunctionTool] | Callable[[Raw_F], RawFunctionTool]'

No documentation available

**Parameters:**

- `f` (F | Raw_F | None) = None
- `name` (str | None) = None
- `description` (str | None) = None
- `raw_schema` (RawFunctionDescription | dict[str, Any] | None) = None


#### is_function_tool(f: 'Callable[..., Any]') -> 'TypeGuard[FunctionTool]'

No documentation available

**Parameters:**

- `f` (Callable[..., Any])


#### is_raw_function_tool(f: 'Callable[..., Any]') -> 'TypeGuard[RawFunctionTool]'

No documentation available

**Parameters:**

- `f` (Callable[..., Any])


### Constants

- `NOT_IN_ALL` = `['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_provider_format', '_strict', 'chat_context', 'fallback_adapter', 'llm', 'realtime', 'tool_context']`
- `n` = `tool_context`

### Examples

```python
# Import livekit.agents.llm
import livekit.agents.llm
```
```python
# Using AudioContent
from livekit.agents.llm import AudioContent


# Call construct
result = instance.construct()
```

```python
# Using ChatChunk
from livekit.agents.llm import ChatChunk


# Call construct
result = instance.construct()
```

```python
# Using ChatContext
from livekit.agents.llm import ChatContext


# Call empty
result = instance.empty()
```

```python
# Using ChatMessage
from livekit.agents.llm import ChatMessage


# Call construct
result = instance.construct()
```

```python
# Using ChoiceDelta
from livekit.agents.llm import ChoiceDelta


# Call construct
result = instance.construct()
```

```python
# Using CompletionUsage
from livekit.agents.llm import CompletionUsage


# Call construct
result = instance.construct()
```

```python
# Using FunctionCall
from livekit.agents.llm import FunctionCall


# Call construct
result = instance.construct()
```

```python
# Using FunctionCallOutput
from livekit.agents.llm import FunctionCallOutput


# Call construct
result = instance.construct()
```

```python
# Using FunctionToolCall
from livekit.agents.llm import FunctionToolCall


# Call construct
result = instance.construct()
```

```python
# Using ImageContent
from livekit.agents.llm import ImageContent


# Call construct
result = instance.construct()
```

```python
# Using LLMError
from livekit.agents.llm import LLMError


# Call construct
result = instance.construct()
```

```python
# Using RealtimeModelError
from livekit.agents.llm import RealtimeModelError


# Call construct
result = instance.construct()
```

```python
# Using ToolContext
from livekit.agents.llm import ToolContext


# Call empty
result = instance.empty()
```


---

## livekit.agents.stt {#livekit-agents-stt}

**Description:** No documentation available

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\agents\stt\__init__.py`

### Classes

#### AvailabilityChangedEvent

AvailabilityChangedEvent(stt: 'STT', available: 'bool')

**Inherits from:** object


#### FallbackAdapter

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** STT


#### RecognitionUsage

RecognitionUsage(audio_duration: 'float')

**Inherits from:** object


#### RecognizeStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC


#### STT

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC, EventEmitter, Generic


#### STTCapabilities

STTCapabilities(streaming: 'bool', interim_results: 'bool')

**Inherits from:** object


#### STTError

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


#### SpeechData

SpeechData(language: 'str', text: 'str', start_time: 'float' = 0.0, end_time: 'float' = 0.0, confidence: 'float' = 0.0, speaker_id: 'str | None' = None)

**Inherits from:** object


#### SpeechEvent

SpeechEvent(type: 'SpeechEventType', request_id: 'str' = '', alternatives: 'list[SpeechData]' = <factory>, recognition_usage: 'RecognitionUsage | None' = None)

**Inherits from:** object


#### SpeechEventType

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to 'utf-8'.
errors defaults to 'strict'.

**Inherits from:** str, Enum


#### SpeechStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC


#### StreamAdapter

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** STT


#### StreamAdapterWrapper

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** RecognizeStream


### Constants

- `NOT_IN_ALL` = `['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'fallback_adapter', 'stream_adapter', 'stt']`
- `n` = `stt`

### Examples

```python
# Import livekit.agents.stt
import livekit.agents.stt
```
```python
# Using STTError
from livekit.agents.stt import STTError


# Call construct
result = instance.construct()
```


---

## livekit.agents.tts {#livekit-agents-tts}

**Description:** No documentation available

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\agents\tts\__init__.py`

### Classes

#### AudioEmitter

No documentation available

**Inherits from:** object


#### AvailabilityChangedEvent

AvailabilityChangedEvent(tts: 'TTS', available: 'bool')

**Inherits from:** object


#### ChunkedStream

Used by the non-streamed synthesize API, some providers support chunked http responses

**Inherits from:** ABC


#### FallbackAdapter

Manages multiple TTS instances, providing a fallback mechanism to ensure continuous TTS service.

**Inherits from:** TTS


#### FallbackChunkedStream

Used by the non-streamed synthesize API, some providers support chunked http responses

**Inherits from:** ChunkedStream


#### FallbackSynthesizeStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** SynthesizeStream


#### StreamAdapter

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** TTS


#### StreamAdapterWrapper

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** SynthesizeStream


#### SynthesizeStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC


#### SynthesizedAudio

SynthesizedAudio(frame: 'rtc.AudioFrame', request_id: 'str', is_final: 'bool' = False, segment_id: 'str' = '', delta_text: 'str' = '')

**Inherits from:** object


#### TTS

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC, EventEmitter, Generic


#### TTSCapabilities

TTSCapabilities(streaming: 'bool')

**Inherits from:** object


#### TTSError

!!! abstract "Usage Documentation"
    [Models](../concepts/models.md)

A base class for creating Pydantic models.

Attributes:
    __class_vars__: The names of the class variables defined on the model.
    __private_attributes__: Metadata about the private attributes of the model.
    __signature__: The synthesized `__init__` [`Signature`][inspect.Signature] of the model.

    __pydantic_complete__: Whether model building is completed, or if there are still undefined fields.
    __pydantic_core_schema__: The core schema of the model.
    __pydantic_custom_init__: Whether the model has a custom `__init__` function.
    __pydantic_decorators__: Metadata containing the decorators defined on the model.
        This replaces `Model.__validators__` and `Model.__root_validators__` from Pydantic V1.
    __pydantic_generic_metadata__: Metadata for generic models; contains data used for a similar purpose to
        __args__, __origin__, __parameters__ in typing-module generics. May eventually be replaced by these.
    __pydantic_parent_namespace__: Parent namespace of the model, used for automatic rebuilding of models.
    __pydantic_post_init__: The name of the post-init method for the model, if defined.
    __pydantic_root_model__: Whether the model is a [`RootModel`][pydantic.root_model.RootModel].
    __pydantic_serializer__: The `pydantic-core` `SchemaSerializer` used to dump instances of the model.
    __pydantic_validator__: The `pydantic-core` `SchemaValidator` used to validate instances of the model.

    __pydantic_fields__: A dictionary of field names and their corresponding [`FieldInfo`][pydantic.fields.FieldInfo] objects.
    __pydantic_computed_fields__: A dictionary of computed field names and their corresponding [`ComputedFieldInfo`][pydantic.fields.ComputedFieldInfo] objects.

    __pydantic_extra__: A dictionary containing extra values, if [`extra`][pydantic.config.ConfigDict.extra]
        is set to `'allow'`.
    __pydantic_fields_set__: The names of fields explicitly set during instantiation.
    __pydantic_private__: Values of private attributes set on the model instance.

**Inherits from:** BaseModel

**Methods:**

- `construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - No documentation available...

- `from_orm(obj: 'Any') -> 'Self'`
 - No documentation available...

- `model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any') -> 'Self'`
 - Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dic...

- `model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation') -> 'dict[str, Any]'`
 - Generates a JSON schema for a model class.

Args:
    by_alias: Whether to use attribute aliases or ...

- `model_parametrized_name(params: 'tuple[type[Any], ...]') -> 'str'`
 - Compute the class name for parametrizations of generic classes.

This method can be overridden to ac...

- `model_rebuild(*, force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None) -> 'bool | None'`
 - Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annota...

- `model_validate(obj: 'Any', *, strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate a pydantic model instance.

Args:
    obj: The object to validate.
    strict: Whether to e...

- `model_validate_json(json_data: 'str | bytes | bytearray', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - !!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate th...

- `model_validate_strings(obj: 'Any', *, strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None) -> 'Self'`
 - Validate the given object with string data against the Pydantic model.

Args:
    obj: The object co...

- `parse_file(path: 'str | Path', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `parse_obj(obj: 'Any') -> 'Self'`
 - No documentation available...

- `parse_raw(b: 'str | bytes', *, content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False) -> 'Self'`
 - No documentation available...

- `schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}') -> 'Dict[str, Any]'`
 - No documentation available...

- `schema_json(*, by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any') -> 'str'`
 - No documentation available...

- `update_forward_refs(**localns: 'Any') -> 'None'`
 - No documentation available...

- `validate(value: 'Any') -> 'Self'`
 - No documentation available...


### Constants

- `NOT_IN_ALL` = `['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'fallback_adapter', 'stream_adapter', 'tts']`
- `n` = `tts`

### Examples

```python
# Import livekit.agents.tts
import livekit.agents.tts
```
```python
# Using TTSError
from livekit.agents.tts import TTSError


# Call construct
result = instance.construct()
```


---

## livekit.api {#livekit-api}

**Description:** LiveKit Server APIs for Python

`pip install livekit-api`

Manage rooms, participants, egress, ingress, SIP, and Agent dispatch.

Primary entry point is `LiveKitAPI`.

See https://docs.livekit.io/reference/server/server-apis for more information.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\api\__init__.py`

### Classes

#### AccessToken

No documentation available

**Inherits from:** object


#### ActiveSpeakerUpdate

A ProtocolMessage

**Inherits from:** Message, Message


#### AgentDispatch

A ProtocolMessage

**Inherits from:** Message, Message


#### AgentDispatchState

A ProtocolMessage

**Inherits from:** Message, Message


#### AliOSSUpload

A ProtocolMessage

**Inherits from:** Message, Message


#### AutoParticipantEgress

A ProtocolMessage

**Inherits from:** Message, Message


#### AutoTrackEgress

A ProtocolMessage

**Inherits from:** Message, Message


#### AvailabilityRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### AvailabilityResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### AzureBlobUpload

A ProtocolMessage

**Inherits from:** Message, Message


#### ChatMessage

A ProtocolMessage

**Inherits from:** Message, Message


#### ClientConfiguration

A ProtocolMessage

**Inherits from:** Message, Message


#### ClientInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### Codec

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateAgentDispatchRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateIngressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateRoomRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateSIPDispatchRuleRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateSIPInboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateSIPOutboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateSIPParticipantRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### CreateSIPTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DataPacket

A ProtocolMessage

**Inherits from:** Message, Message


#### DataStream

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteAgentDispatchRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteIngressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteRoomRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteRoomResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteSIPDispatchRuleRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DeleteSIPTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### DirectFileOutput

A ProtocolMessage

**Inherits from:** Message, Message


#### DisabledCodecs

A ProtocolMessage

**Inherits from:** Message, Message


#### EgressInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### EncodedFileOutput

A ProtocolMessage

**Inherits from:** Message, Message


#### EncodingOptions

A ProtocolMessage

**Inherits from:** Message, Message


#### Encryption

A ProtocolMessage

**Inherits from:** Message, Message


#### FileInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### ForwardParticipantRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ForwardParticipantResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### GCPUpload

A ProtocolMessage

**Inherits from:** Message, Message


#### GetSIPInboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### GetSIPInboundTrunkResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### GetSIPOutboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### GetSIPOutboundTrunkResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ImageOutput

A ProtocolMessage

**Inherits from:** Message, Message


#### ImagesInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressAudioEncodingOptions

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressAudioOptions

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressState

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressVideoEncodingOptions

A ProtocolMessage

**Inherits from:** Message, Message


#### IngressVideoOptions

A ProtocolMessage

**Inherits from:** Message, Message


#### InputAudioState

A ProtocolMessage

**Inherits from:** Message, Message


#### InputVideoState

A ProtocolMessage

**Inherits from:** Message, Message


#### Job

A ProtocolMessage

**Inherits from:** Message, Message


#### JobAssignment

A ProtocolMessage

**Inherits from:** Message, Message


#### JobState

A ProtocolMessage

**Inherits from:** Message, Message


#### JobTermination

A ProtocolMessage

**Inherits from:** Message, Message


#### ListAgentDispatchRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListAgentDispatchResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListEgressResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListIngressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListIngressResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListParticipantsRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListParticipantsResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListRoomsRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListRoomsResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPDispatchRuleRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPDispatchRuleResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPInboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPInboundTrunkResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPOutboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPOutboundTrunkResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ListSIPTrunkResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ListUpdate

A ProtocolMessage

**Inherits from:** Message, Message


#### LiveKitAPI

LiveKit Server API Client

This class is the main entrypoint, which exposes all services.

Usage:

```python
from livekit import api
lkapi = api.LiveKitAPI()
rooms = await lkapi.room.list_rooms(api.proto_room.ListRoomsRequest(names=['test-room']))
```

**Inherits from:** object


#### MigrateJobRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### MoveParticipantRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### MoveParticipantResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### MuteRoomTrackRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### MuteRoomTrackResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### Pagination

A ProtocolMessage

**Inherits from:** Message, Message


#### ParticipantEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### ParticipantInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### ParticipantPermission

A ProtocolMessage

**Inherits from:** Message, Message


#### ParticipantTracks

A ProtocolMessage

**Inherits from:** Message, Message


#### PlayoutDelay

A ProtocolMessage

**Inherits from:** Message, Message


#### ProxyConfig

A ProtocolMessage

**Inherits from:** Message, Message


#### RTCPSenderReportState

A ProtocolMessage

**Inherits from:** Message, Message


#### RTPDrift

A ProtocolMessage

**Inherits from:** Message, Message


#### RTPForwarderState

A ProtocolMessage

**Inherits from:** Message, Message


#### RTPMungerState

A ProtocolMessage

**Inherits from:** Message, Message


#### RTPStats

A ProtocolMessage

**Inherits from:** Message, Message


#### RegisterWorkerRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### RegisterWorkerResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### RemoveParticipantResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### Room

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomAgent

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomAgentDispatch

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomCompositeEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomConfiguration

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomEgress

A ProtocolMessage

**Inherits from:** Message, Message


#### RoomParticipantIdentity

A ProtocolMessage

**Inherits from:** Message, Message


#### RpcAck

A ProtocolMessage

**Inherits from:** Message, Message


#### RpcError

A ProtocolMessage

**Inherits from:** Message, Message


#### RpcRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### RpcResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### S3Upload

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPCallInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRule

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRuleCallee

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRuleDirect

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRuleIndividual

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRuleInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPDispatchRuleUpdate

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPGrants

SIPGrants(admin: bool = False, call: bool = False)

**Inherits from:** object


#### SIPInboundTrunkInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPInboundTrunkUpdate

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPOutboundConfig

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPOutboundTrunkInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPOutboundTrunkUpdate

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPParticipantInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPStatus

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPTransferInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPTrunkInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SIPUri

A ProtocolMessage

**Inherits from:** Message, Message


#### SegmentedFileOutput

A ProtocolMessage

**Inherits from:** Message, Message


#### SegmentsInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SendDataRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### SendDataResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### ServerInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### ServerMessage

A ProtocolMessage

**Inherits from:** Message, Message


#### SimulateJobRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### SimulcastCodecInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### SipDTMF

A ProtocolMessage

**Inherits from:** Message, Message


#### SpeakerInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### StopEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### StreamInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### StreamInfoList

A ProtocolMessage

**Inherits from:** Message, Message


#### StreamOutput

A ProtocolMessage

**Inherits from:** Message, Message


#### TimedVersion

A ProtocolMessage

**Inherits from:** Message, Message


#### TokenVerifier

No documentation available

**Inherits from:** object


#### TrackCompositeEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### TrackEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### TrackInfo

A ProtocolMessage

**Inherits from:** Message, Message


#### Transcription

A ProtocolMessage

**Inherits from:** Message, Message


#### TranscriptionSegment

A ProtocolMessage

**Inherits from:** Message, Message


#### TransferSIPParticipantRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### TwirpError

Common base class for all non-exit exceptions.

**Inherits from:** Exception


#### TwirpErrorCode

No documentation available

**Inherits from:** object


#### UpdateIngressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateJobStatus

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateLayoutRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateParticipantRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateRoomMetadataRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateSIPDispatchRuleRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateSIPInboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateSIPOutboundTrunkRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateStreamRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateSubscriptionsRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateSubscriptionsResponse

A ProtocolMessage

**Inherits from:** Message, Message


#### UpdateWorkerStatus

A ProtocolMessage

**Inherits from:** Message, Message


#### UserPacket

A ProtocolMessage

**Inherits from:** Message, Message


#### VP8MungerState

A ProtocolMessage

**Inherits from:** Message, Message


#### VideoConfiguration

A ProtocolMessage

**Inherits from:** Message, Message


#### VideoGrants

VideoGrants(room_create: Optional[bool] = None, room_list: Optional[bool] = None, room_record: Optional[bool] = None, room_admin: Optional[bool] = None, room_join: Optional[bool] = None, room: str = '', can_publish: bool = True, can_subscribe: bool = True, can_publish_data: bool = True, can_publish_sources: Optional[List[str]] = None, can_update_own_metadata: Optional[bool] = None, ingress_admin: Optional[bool] = None, hidden: Optional[bool] = None, recorder: Optional[bool] = None, agent: Optional[bool] = None)

**Inherits from:** object


#### VideoLayer

A ProtocolMessage

**Inherits from:** Message, Message


#### WebEgressRequest

A ProtocolMessage

**Inherits from:** Message, Message


#### WebhookConfig

A ProtocolMessage

**Inherits from:** Message, Message


#### WebhookEvent

A ProtocolMessage

**Inherits from:** Message, Message


#### WebhookReceiver

No documentation available

**Inherits from:** object


#### WorkerMessage

A ProtocolMessage

**Inherits from:** Message, Message


#### WorkerPing

A ProtocolMessage

**Inherits from:** Message, Message


#### WorkerPong

A ProtocolMessage

**Inherits from:** Message, Message


### Constants

- `AAC` = `2`
- `AUDIO` = `0`
- `AudioCodec` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A65D0>`
- `AudioMixing` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A75F0>`
- `AudioTrackFeature` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A70B0>`
- `BackupCodecPolicy` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6D50>`
- `CAMERA` = `1`
- `CLIENT_INITIATED` = `1`
- `CONNECTION_TIMEOUT` = `14`
- `ClientConfigSetting` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6F30>`
- `ConnectionQuality` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6ED0>`
- `DATA` = `2`
- `DEFAULT_AC` = `0`
- `DEFAULT_FILETYPE` = `0`
- `DEFAULT_MIXING` = `0`
- `DEFAULT_PROTOCOL` = `0`
- `DEFAULT_SEGMENTED_FILE_PROTOCOL` = `0`
- `DEFAULT_VC` = `0`
- `DESCRIPTOR` = `<google._upb._message.FileDescriptor object at 0x00000192A79FD670>`
- `DISABLED` = `1`
- `DUAL_CHANNEL_AGENT` = `1`
- `DUAL_CHANNEL_ALTERNATE` = `2`
- `DUPLICATE_IDENTITY` = `2`
- `DisconnectReason` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6F90>`
- `EGRESS_ABORTED` = `5`
- `EGRESS_ACTIVE` = `1`
- `EGRESS_COMPLETE` = `3`
- `EGRESS_ENDING` = `2`
- `EGRESS_FAILED` = `4`
- `EGRESS_LIMIT_REACHED` = `6`
- `EGRESS_SOURCE_TYPE_SDK` = `1`
- `EGRESS_SOURCE_TYPE_WEB` = `0`
- `EGRESS_STARTING` = `0`
- `ENABLED` = `2`
- `EXCELLENT` = `2`
- `EgressSourceType` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7710>`
- `EgressStatus` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A76B0>`
- `EncodedFileType` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7410>`
- `EncodingOptionsPreset` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7650>`
- `GOOD` = `1`
- `H264_1080P_30` = `2`
- `H264_1080P_30FPS_1_LAYER` = `4`
- `H264_1080P_30FPS_1_LAYER_HIGH_MOTION` = `9`
- `H264_1080P_30FPS_3_LAYERS` = `1`
- `H264_1080P_30FPS_3_LAYERS_HIGH_MOTION` = `6`
- `H264_1080P_60` = `3`
- `H264_540P_25FPS_2_LAYERS` = `2`
- `H264_540P_25FPS_2_LAYERS_HIGH_MOTION` = `7`
- `H264_720P_30` = `0`
- `H264_720P_30FPS_1_LAYER` = `3`
- `H264_720P_30FPS_1_LAYER_HIGH_MOTION` = `8`
- `H264_720P_30FPS_3_LAYERS` = `0`
- `H264_720P_30FPS_3_LAYERS_HIGH_MOTION` = `5`
- `H264_720P_60` = `1`
- `H264_BASELINE` = `1`
- `H264_HIGH` = `3`
- `H264_MAIN` = `2`
- `HIGH` = `2`
- `HLS_PROTOCOL` = `1`
- `IC_DEFAULT` = `0`
- `IC_JPEG` = `1`
- `IMAGE_SUFFIX_INDEX` = `0`
- `IMAGE_SUFFIX_NONE_OVERWRITE` = `2`
- `IMAGE_SUFFIX_TIMESTAMP` = `1`
- `INDEX` = `0`
- `ImageCodec` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6CF0>`
- `ImageFileSuffix` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7530>`
- `IngressAudioEncodingPreset` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7830>`
- `IngressInput` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A77D0>`
- `IngressVideoEncodingPreset` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7890>`
- `JOIN_FAILURE` = `7`
- `JS_FAILED` = `3`
- `JS_PENDING` = `0`
- `JS_RUNNING` = `1`
- `JS_SUCCESS` = `2`
- `JT_PARTICIPANT` = `2`
- `JT_PUBLISHER` = `1`
- `JT_ROOM` = `0`
- `JobStatus` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A71D0>`
- `JobType` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7110>`
- `KRISP_ENABLED` = `1`
- `LOST` = `3`
- `LOW` = `0`
- `MEDIUM` = `1`
- `MICROPHONE` = `2`
- `MIGRATION` = `8`
- `MP4` = `1`
- `NONE` = `0`
- `OFF` = `3`
- `OGG` = `2`
- `OPUS` = `1`
- `OPUS_MONO_64KBS` = `1`
- `OPUS_STEREO_96KBPS` = `0`
- `PARTICIPANT_REMOVED` = `4`
- `POOR` = `0`
- `PORTRAIT_H264_1080P_30` = `6`
- `PORTRAIT_H264_1080P_60` = `7`
- `PORTRAIT_H264_720P_30` = `4`
- `PORTRAIT_H264_720P_60` = `5`
- `PREFER_REGRESSION` = `0`
- `REGRESSION` = `2`
- `ROOM_CLOSED` = `10`
- `ROOM_DELETED` = `5`
- `RR_PUBLISHER_FAILED` = `2`
- `RR_SIGNAL_DISCONNECTED` = `1`
- `RR_SUBSCRIBER_FAILED` = `3`
- `RR_SWITCH_CANDIDATE` = `4`
- `RR_UNKNOWN` = `0`
- `RTMP` = `1`
- `RTMP_INPUT` = `0`
- `ReconnectReason` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6FF0>`
- `SCD_INBOUND` = `1`
- `SCD_OUTBOUND` = `2`
- `SCD_UNKNOWN` = `0`
- `SCREEN_SHARE` = `3`
- `SCREEN_SHARE_AUDIO` = `4`
- `SCS_ACTIVE` = `2`
- `SCS_CALL_INCOMING` = `0`
- `SCS_DISCONNECTED` = `3`
- `SCS_ERROR` = `4`
- `SCS_PARTICIPANT_JOINED` = `1`
- `SERVER_SHUTDOWN` = `3`
- `SE_CODEC_UNSUPPORTED` = `1`
- `SE_TRACK_NOTFOUND` = `2`
- `SE_UNKNOWN` = `0`
- `SIGNAL_CLOSE` = `9`
- `SIMULCAST` = `1`
- `SIPCallDirection` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A10710>`
- `SIPCallStatus` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A105F0>`
- `SIPFeature` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A106B0>`
- `SIPHeaderOptions` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A10530>`
- `SIPMediaEncryption` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A10590>`
- `SIPStatusCode` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A10350>`
- `SIPTransferStatus` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A10650>`
- `SIPTransport` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A7A104D0>`
- `SIP_ALL_HEADERS` = `2`
- `SIP_MEDIA_ENCRYPT_ALLOW` = `1`
- `SIP_MEDIA_ENCRYPT_DISABLE` = `0`
- `SIP_MEDIA_ENCRYPT_REQUIRE` = `2`
- `SIP_NO_HEADERS` = `0`
- `SIP_STATUS_ACCEPTED` = `202`
- `SIP_STATUS_ADDRESS_INCOMPLETE` = `484`
- `SIP_STATUS_AMBIGUOUS` = `485`
- `SIP_STATUS_BAD_EXTENSION` = `420`
- `SIP_STATUS_BAD_GATEWAY` = `502`
- `SIP_STATUS_BAD_REQUEST` = `400`
- `SIP_STATUS_BUSY_HERE` = `486`
- `SIP_STATUS_CALL_IS_FORWARDED` = `181`
- `SIP_STATUS_CALL_TRANSACTION_DOES_NOT_EXISTS` = `481`
- `SIP_STATUS_CONFLICT` = `409`
- `SIP_STATUS_EXTENSION_REQUIRED` = `421`
- `SIP_STATUS_FORBIDDEN` = `403`
- `SIP_STATUS_GATEWAY_TIMEOUT` = `504`
- `SIP_STATUS_GLOBAL_BUSY_EVERYWHERE` = `600`
- `SIP_STATUS_GLOBAL_DECLINE` = `603`
- `SIP_STATUS_GLOBAL_DOES_NOT_EXIST_ANYWHERE` = `604`
- `SIP_STATUS_GLOBAL_NOT_ACCEPTABLE` = `606`
- `SIP_STATUS_GONE` = `410`
- `SIP_STATUS_INTERNAL_SERVER_ERROR` = `500`
- `SIP_STATUS_INTERVAL_TOO_BRIEF` = `423`
- `SIP_STATUS_LOOP_DETECTED` = `482`
- `SIP_STATUS_MESSAGE_TOO_LARGE` = `513`
- `SIP_STATUS_METHOD_NOT_ALLOWED` = `405`
- `SIP_STATUS_MOVED_PERMANENTLY` = `301`
- `SIP_STATUS_MOVED_TEMPORARILY` = `302`
- `SIP_STATUS_NOTFOUND` = `404`
- `SIP_STATUS_NOT_ACCEPTABLE` = `406`
- `SIP_STATUS_NOT_ACCEPTABLE_HERE` = `488`
- `SIP_STATUS_NOT_IMPLEMENTED` = `501`
- `SIP_STATUS_OK` = `200`
- `SIP_STATUS_PAYMENT_REQUIRED` = `402`
- `SIP_STATUS_PROXY_AUTH_REQUIRED` = `407`
- `SIP_STATUS_QUEUED` = `182`
- `SIP_STATUS_REQUESTED_RANGE_NOT_SATISFIABLE` = `416`
- `SIP_STATUS_REQUEST_ENTITY_TOO_LARGE` = `413`
- `SIP_STATUS_REQUEST_TERMINATED` = `487`
- `SIP_STATUS_REQUEST_TIMEOUT` = `408`
- `SIP_STATUS_REQUEST_URI_TOO_LONG` = `414`
- `SIP_STATUS_RINGING` = `180`
- `SIP_STATUS_SERVICE_UNAVAILABLE` = `503`
- `SIP_STATUS_SESSION_PROGRESS` = `183`
- `SIP_STATUS_TEMPORARILY_UNAVAILABLE` = `480`
- `SIP_STATUS_TOO_MANY_HOPS` = `483`
- `SIP_STATUS_TRYING` = `100`
- `SIP_STATUS_UNAUTHORIZED` = `401`
- `SIP_STATUS_UNKNOWN` = `0`
- `SIP_STATUS_UNSUPPORTED_MEDIA_TYPE` = `415`
- `SIP_STATUS_USE_PROXY` = `305`
- `SIP_STATUS_VERSION_NOT_SUPPORTED` = `505`
- `SIP_TRANSPORT_AUTO` = `0`
- `SIP_TRANSPORT_TCP` = `2`
- `SIP_TRANSPORT_TLS` = `3`
- `SIP_TRANSPORT_UDP` = `1`
- `SIP_TRUNK_FAILURE` = `13`
- `SIP_X_HEADERS` = `1`
- `SRT` = `2`
- `STATE_MISMATCH` = `6`
- `STS_TRANSFER_FAILED` = `1`
- `STS_TRANSFER_ONGOING` = `0`
- `STS_TRANSFER_SUCCESSFUL` = `2`
- `SegmentedFileProtocol` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7470>`
- `SegmentedFileSuffix` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A74D0>`
- `StreamProtocol` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7590>`
- `SubscriptionError` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7050>`
- `TF_AUTO_GAIN_CONTROL` = `2`
- `TF_ECHO_CANCELLATION` = `3`
- `TF_ENHANCED_NOISE_CANCELLATION` = `5`
- `TF_NOISE_SUPPRESSION` = `4`
- `TF_NO_DTX` = `1`
- `TF_PRECONNECT_BUFFER` = `6`
- `TF_STEREO` = `0`
- `TIMESTAMP` = `1`
- `TrackSource` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6E10>`
- `TrackType` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6DB0>`
- `UNKNOWN` = `0`
- `UNKNOWN_REASON` = `0`
- `UNSET` = `0`
- `URL_INPUT` = `2`
- `USER_REJECTED` = `12`
- `USER_UNAVAILABLE` = `11`
- `VIDEO` = `1`
- `VP8` = `4`
- `VideoCodec` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6C90>`
- `VideoQuality` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A6E70>`
- `WHIP_INPUT` = `1`
- `WS_AVAILABLE` = `0`
- `WS_FULL` = `1`
- `WorkerStatus` = `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x00000192A79A7170>`

### Examples

```python
# Import livekit.api
import livekit.api
```

---

## livekit.plugins {#livekit-plugins}

**Description:** No documentation available

### Examples

```python
# Import livekit.plugins
import livekit.plugins
```

---

## livekit.plugins.cartesia {#livekit-plugins-cartesia}

**Description:** Cartesia plugin for LiveKit Agents

See https://docs.livekit.io/agents/integrations/tts/cartesia/ for more information.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\plugins\cartesia\__init__.py`

### Classes

#### CartesiaPlugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** Plugin

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### ChunkedStream

Synthesize chunked text using the bytes endpoint

**Inherits from:** ChunkedStream


#### Plugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### STT

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** STT


#### TTS

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** TTS


### Constants

- `NOT_IN_ALL` = `['CartesiaPlugin', 'Plugin', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'log', 'logger', 'models', 'stt', 'tts', 'version']`
- `logger` = `<Logger livekit.plugins.cartesia (WARNING)>`
- `n` = `version`

### Examples

```python
# Import livekit.plugins.cartesia
import livekit.plugins.cartesia
```
```python
# Using CartesiaPlugin
from livekit.plugins.cartesia import CartesiaPlugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using Plugin
from livekit.plugins.cartesia import Plugin


# Call register_plugin
result = instance.register_plugin()
```


---

## livekit.plugins.deepgram {#livekit-plugins-deepgram}

**Description:** Deepgram plugin for LiveKit Agents

Support for speech-to-text with [Deepgram](https://deepgram.com/).

See https://docs.livekit.io/agents/integrations/stt/deepgram/ for more information.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\plugins\deepgram\__init__.py`

### Classes

#### AudioEnergyFilter

No documentation available

**Inherits from:** object


#### DeepgramPlugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** Plugin

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### Plugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### STT

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** STT


#### SpeechStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** RecognizeStream


#### TTS

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** TTS


### Constants

- `NOT_IN_ALL` = `['DeepgramPlugin', 'Plugin', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_utils', 'log', 'logger', 'models', 'stt', 'tts', 'version']`
- `logger` = `<Logger livekit.plugins.deepgram (WARNING)>`
- `n` = `version`

### Examples

```python
# Import livekit.plugins.deepgram
import livekit.plugins.deepgram
```
```python
# Using DeepgramPlugin
from livekit.plugins.deepgram import DeepgramPlugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using Plugin
from livekit.plugins.deepgram import Plugin


# Call register_plugin
result = instance.register_plugin()
```


---

## livekit.plugins.openai {#livekit-plugins-openai}

**Description:** OpenAI plugin for LiveKit Agents

Support for OpenAI Realtime API, LLM, TTS, and STT APIs.

Also includes support for a large number of OpenAI-compatible APIs including Azure OpenAI, Cerebras,
Fireworks, Perplexity, Telnyx, xAI, Ollama, and DeepSeek.

See https://docs.livekit.io/agents/integrations/openai/ and
https://docs.livekit.io/agents/integrations/llm/ for more information.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\plugins\openai\__init__.py`

### Classes

#### EmbeddingData

EmbeddingData(index: 'int', embedding: 'list[float]')

**Inherits from:** object


#### LLM

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** LLM


#### LLMStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** LLMStream


#### OpenAIPlugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** Plugin

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### Plugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### STT

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** STT


#### TTS

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** TTS


### Functions

#### create_embeddings(*, input: 'list[str]', model: 'models.EmbeddingModels' = 'text-embedding-3-small', dimensions: 'int | None' = None, api_key: 'str | None' = None, http_session: 'aiohttp.ClientSession | None' = None) -> 'list[EmbeddingData]'

No documentation available

**Parameters:**

- `input` (list[str])
- `model` (models.EmbeddingModels) = text-embedding-3-small
- `dimensions` (int | None) = None
- `api_key` (str | None) = None
- `http_session` (aiohttp.ClientSession | None) = None


### Constants

- `NOT_IN_ALL` = `['OpenAIPlugin', 'Plugin', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'embeddings', 'llm', 'log', 'logger', 'models', 'stt', 'tts', 'utils', 'version']`
- `logger` = `<Logger livekit.plugins.openai (WARNING)>`
- `n` = `version`

### Examples

```python
# Import livekit.plugins.openai
import livekit.plugins.openai
```
```python
# Using OpenAIPlugin
from livekit.plugins.openai import OpenAIPlugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using Plugin
from livekit.plugins.openai import Plugin


# Call register_plugin
result = instance.register_plugin()
```


---

## livekit.plugins.silero {#livekit-plugins-silero}

**Description:** Silero VAD plugin for LiveKit Agents

See https://docs.livekit.io/agents/build/turns/vad/ for more information.

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\plugins\silero\__init__.py`

### Classes

#### Plugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** ABC

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### SileroPlugin

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** Plugin

**Methods:**

- `register_plugin(plugin: 'Plugin') -> 'None'`
 - No documentation available...


#### VAD

Silero Voice Activity Detection (VAD) class.

This class provides functionality to detect speech segments within audio data using the Silero VAD model.

**Inherits from:** VAD

**Methods:**

- `load(*, min_speech_duration: 'float' = 0.05, min_silence_duration: 'float' = 0.55, prefix_padding_duration: 'float' = 0.5, max_buffered_speech: 'float' = 60.0, activation_threshold: 'float' = 0.5, sample_rate: 'Literal[8000, 16000]' = 16000, force_cpu: 'bool' = True, padding_duration: 'NotGivenOr[float]' = NOT_GIVEN) -> 'VAD'`
 - Load and initialize the Silero VAD model.

This method loads the ONNX model and prepares it for infe...


#### VADStream

Helper class that provides a standard way to create an ABC using
inheritance.

**Inherits from:** VADStream


### Constants

- `NOT_IN_ALL` = `['Plugin', 'SileroPlugin', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'log', 'logger', 'onnx_model', 'vad', 'version']`
- `logger` = `<Logger livekit.plugins.silero (WARNING)>`
- `n` = `version`

### Examples

```python
# Import livekit.plugins.silero
import livekit.plugins.silero
```
```python
# Using Plugin
from livekit.plugins.silero import Plugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using SileroPlugin
from livekit.plugins.silero import SileroPlugin


# Call register_plugin
result = instance.register_plugin()
```

```python
# Using VAD
from livekit.plugins.silero import VAD


# Call load
result = instance.load()
```


---

## livekit.protocol {#livekit-protocol}

**Description:** No documentation available

**File:** `C:\projects\letta-voice\venv\Lib\site-packages\livekit\protocol\__init__.py`

### Examples

```python
# Import livekit.protocol
import livekit.protocol
```

---
