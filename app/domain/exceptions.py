class DomainError(Exception):
    """Erro base para violações de regras de domínio."""


class InvalidCustomerIdError(DomainError):
    """Customer ID inválido."""


class InvalidServiceTypeError(DomainError):
    """Tipo de serviço inválido."""


class InvalidBandwidthError(DomainError):
    """Largura de banda inválida."""


class InvalidLocationError(DomainError):
    """Localização inválida."""