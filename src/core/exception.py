import dataclasses


@dataclasses.dataclass(frozen=True, slots=True)
class ModelAlreadyExistsError:
    identifier: str
    message: str = "Model already exists"


@dataclasses.dataclass(frozen=True, slots=True)
class NotFoundCoreError:
    identifier: str
    message: str
