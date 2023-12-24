import abc
import asyncio
from concurrent.futures import ProcessPoolExecutor


class AbstractModel:
    @abc.abstractmethod
    def compute(self):
        ...


class Handler:
    def __init__(self, model: AbstractModel):
        self._model = model

    async def handle_request(self) -> None:
        # Модель выполняет некий тяжёлый код (ознакомьтесь с ним в файле тестов),
        # вам необходимо добиться его эффективного конкурентного исполнения.
        #
        # Тест проверяет, что время исполнения одной корутины handle_request не слишком сильно
        # отличается от времени исполнения нескольких таких корутин, запущенных конкурентно.
        #
        # YOU CODE GOES HERE
        with ProcessPoolExecutor(max_workers=10) as executor:
            task = asyncio.create_task(self.process_task(executor))
            await task

    async def process_task(self, executor: ProcessPoolExecutor):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(executor, self._model.compute())
