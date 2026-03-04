from abc import ABC, abstractmethod

from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: str) -> User | None:
        """Retrieve a user by their unique ID."""
        raise NotImplementedError
    
    @abstractmethod
    def get_by_username(self, username: str) -> User | None:
        """Retrieve a user by their username."""
        raise NotImplementedError
    
    @abstractmethod
    def save(self, user: User) -> None:
        """Persist a user entity to the repository."""
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, user_id: str) -> None:
        """Delete a user by their unique ID."""
        raise NotImplementedError