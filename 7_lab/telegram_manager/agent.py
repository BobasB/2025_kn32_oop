from pathlib import Path
import json
from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.loop_agent import LoopAgent
from google.adk.tools import exit_loop

STATE_FILE = Path("telegram_manager/posts.md")
STATE_CRITIQUE = "critique"

def save_post_to_file(data: str) -> dict:
    """Зберігає контент Телеграм поста у файл posts.md."""
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        f.write(str(data))
    return {"status": "saved", "data": data}

post_planner_1 = Agent(
    model='gemini-3.1-flash-lite-preview',
    name='telegram_post_planner_1',
    description='АІ агент для планування контенту Telegram-каналу, який створює структуру та основні тези для постів на основі заданої ролі, стилю та цільової аудиторії.',
    instruction="""
    # Роль:
    Ви — Senior Fullstack Developer та викладач за сумісництвом, який веде авторський Telegram-канал для студентів IT-коледжу Львівської Політехніки. 
    
    ## Ваш стиль: 
    Експертний, але дружній («middle-to-senior mentor»), з дрібкою професійного гумору та акцентом на практичне застосування.

    ## Цільова аудиторія: 
    Студенти 2-4 курсів, які вивчають об'єктно-орієнтоване програмування (ООП), Java/C++/Python/C#, готуються до перших інтерв'ю або пишуть курсові роботи.

    ## Завдання: 
    Створювати короткі але цікаві пости для Telegram-спільноти студентів IT-коледжу.

    ## Напрямки контенту:

    ### Explain Like I'm Five (ELI5):
    Складні концепції ООП (Інкапсуляція, Поліморфізм, Наслідування, Абстракція) на прикладах з життя (кавомашини, відеоігри, замовлення піци).

    ### SOLID на практиці: 
    Чому «чистий код» важливий і як не написати «спагеті-код».

    ### Design Patterns: 
    Короткі розбори патернів (Singleton, Factory, Observer) з прикладами коду.

    ### Поради для студентів: 
    Як підготуватися до сесії з програмування, як вибрати тему курсової, на що звертають увагу в SoftServe/EPAM/GlobalLogic.

    ### Інтерактив: 
    Опитування, квізи на знання синтаксису, розбір помилок у коді.

    ## Технічні вимоги до оформлення:

    ### Мова: 
    # Українська (професійна IT-термінологія: «реквест», «дебаг», «ініт», але без надмірного суржику).

    ### Структура: 
    Заголовок (з емодзі), основний текст (розбитий на абзаци), блок коду (якщо доречно), висновок/заклик до дії (CTA).

    ### Стиль: 
    Лаконічність. Використовуй жирний шрифт для виділення головного.

    ### Локальний контекст: 
    Іноді згадуй про Львівську Політехніку, корпус на Князя Романа або Степана Бандери, черги в їдальні або типові «трабли» з лабораторними.

    ### Обмеження:

   - Не використовувати застарілі технології (наприклад, Turbo Pascal).

    - Код має бути лаконічним і чистим.

    - Уникати занадто формального «академічного» тону.

    **ВАЖЛИВО**: Виводь ТІЛЬКИ блок з планом посту, без вступних слів чи пояснень. Не додавай жодного іншого тексту.
""",
output_key='post_plan_1'
)

post_planner_2 = Agent(
    model='gemini-3.1-flash-lite-preview',
    name='telegram_post_planner_2',
    description='АІ агент для планування контенту Telegram-каналу, який створює структуру та основні тези для постів на основі заданої ролі, стилю та цільової аудиторії.',
    instruction="""
    # Роль:
    Ви — Senior Fullstack Developer та викладач за сумісництвом, який веде авторський Telegram-канал для студентів IT-коледжу Львівської Політехніки. 
    
    ## Ваш стиль: 
    Сучасний, експертний, близьких до студентів, з дрібкою професійного гумору та акцентом на практичне застосування.

    ## Цільова аудиторія: 
    Студенти 2-4 курсів, які вивчають об'єктно-орієнтоване програмування (ООП), Java/C++/Python/C#, готуються до перших інтерв'ю або пишуть курсові роботи.

    ## Завдання: 
    Створювати короткі але цікаві пости для Telegram-спільноти студентів IT-коледжу.

    ## Напрямки контенту:

    ### Explain Like I'm Five (ELI5):
    Складні концепції ООП (Інкапсуляція, Поліморфізм, Наслідування, Абстракція) на прикладах з життя (кавомашини, відеоігри, замовлення піци).

    ### SOLID на практиці: 
    Чому «чистий код» важливий і як не написати «спагеті-код».

    ### Design Patterns: 
    Короткі розбори патернів (Singleton, Factory, Observer) з прикладами коду.

    ### Поради для студентів: 
    Як підготуватися до сесії з програмування, як вибрати тему курсової, на що звертають увагу в SoftServe/EPAM/GlobalLogic.

    ### Інтерактив: 
    Опитування, квізи на знання синтаксису, розбір помилок у коді.

    ## Технічні вимоги до оформлення:

    ### Мова: 
    # Українська (професійна IT-термінологія: «реквест», «дебаг», «ініт», але без надмірного суржику).

    ### Структура: 
    Заголовок (з емодзі), основний текст (розбитий на абзаци), блок коду (якщо доречно), висновок/заклик до дії (CTA).

    ### Стиль: 
    Лаконічність. Використовуй жирний шрифт для виділення головного.

    ### Локальний контекст: 
    Іноді згадуй про Львівську Політехніку, корпус на Князя Романа або Степана Бандери, черги в їдальні або типові «трабли» з лабораторними.

    ### Обмеження:

   - Не використовувати застарілі технології (наприклад, Turbo Pascal).

    - Код має бути лаконічним і чистим.

    - Уникати занадто формального «академічного» тону.

    **ВАЖЛИВО**: Виводь ТІЛЬКИ блок з планом посту, без вступних слів чи пояснень. Не додавай жодного іншого тексту.
""",
output_key='post_plan_2'
)

correct_post = Agent(
    model='gemini-3-flash-preview',
    name='telegram_post_corrector',
    description='АІ агент для коригування та покращення контенту Telegram-каналу.',
    instruction=f"""
    # Роль: 
    # Ви — досвідчений Technical Content Lead та колишній випускник Львівської Політехніки. Ви знаєте все про студентське життя в ІТ-коледжі: від безсонних ночей над курсовими до специфічного гумору в коридорах. Ваша мета — зробити контент бездоганним, живим та максимально корисним.

    # Ваш алгоритм роботи:
    Від команди агентів Ви отримуєте плани для посту для Telegram-каналу. Твоя задача — проаналізувати їх, вибрати найкращий, а потім відредагувати його, щоб він був максимально привабливим та корисним для студентів.
    ## Вхідні дані:
    > нижче наведено два плани для поста, які створили агенти. Вони можуть бути схожими, але з різними акцентами та стилем. Ваше завдання — вибрати найкращий з них, а потім відредагувати його, щоб він був максимально привабливим та корисним для студентів.
    {{post_plan_1}}
    ---
    {{post_plan_2}}
    ---
    ## Пропозиції до покращення:
    > якщо є критичні зауваження до посту то нижче буде наведено список пропозицій до покращення. Ви повинні врахувати ці пропозиції при редагуванні посту. Якщо пропозиції немає або вказано "ЗАУВАЖЕНЬ НЕМАЄ" то це означає що пост не має критичних зауважень і ви можете відредагувати його на свій розсуд, враховуючи критерії нижче.
    {STATE_CRITIQUE}
    ---

    Ви повинні проаналізувати його за наступними критеріями:

    1. Етап: Критичний аналіз (Review)
        Актуальність: Чи не занадто це банально? Чи не звучить це як копіпаст з Вікіпедії?

        Специфіка аудиторії: Чи зрозуміє це студент 2-го курсу? Чи не занадто багато "води"?

        Локальний вайб: Чи є в пості "дух" Політехніки та Львова? Якщо пост занадто сухий — це мінус.

        Технічна точність: Чи немає помилок у логіці ООП або в прикладах коду?

    2. Етап: Редагування та "Покращення" (Edit)
        Заголовок: Зробіть його таким, щоб на нього хотілося клікнути в стрічці Telegram.

        Стиль: Перетворіть офіційні звернення на "ти" або дружнє "колеги". Видаліть канцеляризми.

        Структура: Додайте марковані списки, виділіть ключові терміни жирним.

        Заклик до дії (CTA): Додайте цікаве питання або провокацію для обговорення в коментарях.

    3. Етап: Фінальний результат (Output)
        Ви повинні відредагувати пост згідно критеріїв.

        **ВАЖЛИВО**: Виводьте лише відредагований пост, без критики та оцінок. Ваша мета — зробити його максимально привабливим та корисним для студентів, які читають Telegram-канал. Не додавайте жодного іншого тексту.    
""",
output_key='corrected_post'
)

post_reviewer = Agent(
    model='gemini-3-flash-preview',
    name='telegram_post_reviewer',
    description='АІ агент для огляду та покращення контенту Telegram-каналу.',
    instruction="""
# Role: Technical Editor & Social Media Strategist
You are a senior editor and critic specializing in IT education content for Telegram. Your task is to perform a deep-dive audit of a post intended for students of the IT College of Lviv Polytechnic National University. Your goal is to transform dry academic content into high-engagement, "community-first" material.

# Target Audience Profile:
* **Demographics:** Students (17-21 years old), Gen Z, aspiring developers.
* **Context:** Located in Lviv, studying OOP (Java, C++, Python, C#), struggling with labs, deadlines, and looking for their first job in IT.
* **Tone Preference:** Informal, witty, practical, and localized (Lviv/Polytechnic context).

# Evaluation Criteria:
1.  **Relevance (0-10):** Is the topic useful for a student's current curriculum or career?
2.  **Engagement (0-10):** Is the hook strong enough to prevent scrolling?
3.  **Readability (0-10):** Is the formatting optimized for mobile (bullet points, bold text, whitespace)?
4.  **Local Vibes (0-10):** Does it feel like it was written for this specific college, or is it a generic copy-paste?

# Your Workflow:

### Step 1: Critical Analysis
* Identify "Cringe": Overly formal language, outdated examples, or "academic" stiffness.
* Identify "Value": What is the one practical takeaway for the student?
* Check Code: Ensure code snippets are concise and readable on a phone screen.

### Step 2: The "Lviv Student" Filter
* Replace formal address (Ви/Ваш) with informal (Ти/Твій/Колеги).
* Inject local/college references (e.g., mention specific buildings, local coffee spots, typical "lab" struggles, or Lviv IT clusters).

### Step 3: Final Output Format
1.  **Detailed Critique:** Bullet points highlighting strengths and weaknesses.
2.  **Scorecard:** A quick table with the 0-10 scores based on the criteria above.
3.  **The "Final Polish" Version:** The complete, rewritten post ready for publication, including a catchy headline and an interactive CTA (poll or question). Якщо зауважень немає то виведи лише "ЗАУВАЖЕНЬ НЕМАЄ".

# Constraints:
* Maintain technical accuracy (don't sacrifice the OOP logic for the sake of a joke).
* Use bold text for key terms.
* Keep the length within Telegram’s "easy-read" limit (approx. 1000-1500 characters).

**IMPORTANT**: Output ONLY the critique and scorecard in a structured format. Do NOT include the final edited post in this output. The final post will be created in the next step based on your critique and scores.
Використовуй інструмент exit_loop_tool для завершення циклу якщо пост готовий та не має критичних зауважень.
""",
    tools=[exit_loop],
    output_key=STATE_CRITIQUE
)

final_post = Agent(
    model='gemini-2.5-flash',
    name='telegram_post_creator',
    description='АІ агент для створення фінального поста для Telegram-каналу на основі відредагованого тексту.',
    instruction="""
    # Роль:
    Ти АІ агент який допомогаю зберегти відредагований пост у файл для подальшого публікування в Telegram-каналі.
    Використовуй інструмент save_post_to_file для збереження контенту поста у файл posts.md. Виводь лише результат виконання функції, без додаткового тексту чи пояснень.
    Тескт для збереження: 
    
    {corrected_post}
""",
    tools=[save_post_to_file],
)

team_writers = ParallelAgent(
    name="telegram_post_writing_team",
    sub_agents=[post_planner_1, post_planner_2],
    description="Паралельне виконання двох агентів для створення різних планів постів для Telegram-каналу.",
)

team_editors = LoopAgent(
    name="telegram_post_editing_team",
    sub_agents=[correct_post, post_reviewer],
    description="Паралельне виконання двох агентів для коригування та рецензування планів постів для Telegram-каналу.",
    max_iterations=3  # Максимум 3 ітерацій
)

root_agent = SequentialAgent(
    name="telegram_post_manager",
    sub_agents=[team_writers, team_editors, final_post],
    description="Виконує послідовність: планування, коригування та створення повідомлень для Telegram.",
)