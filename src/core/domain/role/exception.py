import dataclasses


@dataclasses.dataclass(frozen=True, slots=True)
class RoleAlreadyExistsError:
    identifier: str
    message: str = "Role already exists"


@dataclasses.dataclass(frozen=True, slots=True)
class NotFoundCoreError:
    identifier: str
    message: str
