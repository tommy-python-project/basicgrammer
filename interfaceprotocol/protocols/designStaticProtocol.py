"""
设计静态协议
"""
from typing import Protocol, Any, List


class DatabaseConnection(Protocol):
    def connect(self,connection_string: str) -> None:
        ...
    def execute(self,query: str,params: List[Any] = None) -> List[Any]: ...

    def close(self) -> None: ...


class PostgreSQLConnection:
    def connect(self,connection_string: str) -> None:
        print(f"Connecting to PostgreSQL: {connection_string}")

    def execute(self, query: str, params: List[Any] = None) -> List[Any]:
        print(f"Executing: {query}")
        return [("result1",), ("result2",)]

    def close(self) -> None:
        print("Closing PostgreSQL connection")

def use_database(db: DatabaseConnection,conn_str: str,query: str) :
    db.connect(conn_str)
    try:
        results = db.execute(query)
        return results
    finally:
        db.close()

postgres = PostgreSQLConnection()
results = use_database(postgres, "host=localhost", "SELECT * FROM users")