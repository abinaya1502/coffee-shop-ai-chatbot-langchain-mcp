from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from setting import config

class Database:
    def __init__(self):
        self.engine = self._create_engine()
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False
        )

    def _create_engine(self):
        db_url = (
            f"postgresql+psycopg2://{config.db_username}:"
            f"{config.db_password}@"
            f"{config.db_host}:"
            f"{config.db_port}/"
            f"{config.db_name}"
        )
        return create_engine(db_url)

    async def get_session(self):
        try:
            session = self.SessionLocal()
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            
    def inspector(self, engine):
        return inspect(engine)
    
    async def test_connection(self):
        """Test database connection"""
        try:
            with self.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            return True
        except Exception:
            return False