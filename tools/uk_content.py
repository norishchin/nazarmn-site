"""Ukrainian pages: /uk/, /uk/buy/, /uk/sell/, /uk/commercial/, /uk/blog/ and /uk/blog/<slug>/."""
import datetime
import json
import re

from uk_posts import UK_POSTS

MONTHS = ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня", "листопада", "грудня"]
BOOK_BTN = '<a class="btn primary" href="/book/">Запишіться на 15-хвилинну розмову</a>'
NOTE_EN = '<p class="soft" style="font-size:14px">Відгуки наведено мовою оригіналу, як їх написали клієнти в Google.</p>'


def uk_date(d):
    d = datetime.date.fromisoformat(d)
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def build_uk(g):
    page, card, next_step, newsletter, quote, pull = g["page"], g["card"], g["next_step"], g["newsletter"], g["quote"], g["pull"]
    SEARCH, SITE, POSTS, CAT_UK = g["SEARCH"], g["SITE"], g["POSTS"], g["CAT_UK"]
    by = {p["slug"]: p for p in POSTS}
    for p in POSTS:
        u = dict(UK_POSTS[p["slug"]])
        u["mins"] = p["mins"]
        p["uk"] = u

    # ---------- home ----------
    home = f"""
<div class="wrap hero" id="top">
<div class="stack lg">
<p class="label">RE/MAX Results · Team Steady · Ліцензія Міннесоти</p>
<h1>Купуйте, продавайте та інвестуйте в Міннесоті з агентом, який рахує цифри.</h1>
<p class="lead">Мене звати Назар Оріщин. П'ять років я працював інженером, перш ніж прийти в нерухомість, тому кожну ціну, пропозицію та інвестицію перевіряю як технічну специфікацію, перш ніж ви підпишете. Усе пояснюю українською.</p>
<div class="cta">{BOOK_BTN}<a class="arrow" href="{SEARCH}" target="_blank" rel="noopener">Пошук будинків на продаж</a></div>
</div>
<div class="photo"><img src="/images/nazar-orishchin.jpg" alt="Назар Оріщин, агент з нерухомості" width="900" height="1350" fetchpriority="high"></div>
</div>

<section class="rule" aria-label="Коротко"><div class="wrap section tight stats">
<div class="stat"><b>100+</b><span>Угод закрито з 2022 року</span></div>
<div class="stat"><b>5.0</b><span>Рейтинг у Google з 26 відгуків</span></div>
<div class="stat"><b>5 років</b><span>Інженером до нерухомості</span></div>
<div class="stat"><b>2</b><span>Мови: українська та англійська</span></div>
</div></section>

<section class="rule"><div class="wrap section split">
<div class="stack"><p class="chapter">01 · Проблема</p><h2>Ви робите це кілька разів у житті. Інша сторона робить це щодня.</h2></div>
<div class="stack">
<p class="lead">Купівля чи продаж будинку або будівлі є найбільшим чеком, який більшість людей підписує в житті. Агент продавця, сам продавець і кредитор роблять це щотижня. Ви заслуговуєте на когось на вашому боці, хто теж робить це постійно і перевіряє розрахунки.</p>
<p>Це моя робота: з'ясувати, скільки об'єкт вартий насправді, скільки він вам насправді коштуватиме і як закрити угоду без сюрпризів. А потім сказати вам прямо, навіть якщо відповідь: «відмовтеся».</p>
<p>Я народився в Україні і переїхав до Міннесоти у три роки. Для багатьох моїх клієнтів найбільша перевага в тому, що договір, інспекцію і кредит можна обговорити рідною мовою.</p>
</div>
</div></section>

<section class="rule"><div class="wrap section stack lg" id="help">
<div class="stack"><p class="chapter">02 · Чим я допомагаю</p><h2>Оберіть, де ви зараз.</h2></div>
<div class="grid g3">
<a class="card" href="/uk/buy/"><p class="label">Купівля будинку</p><h3>Знайти правильний будинок і заплатити правильну ціну.</h3><p class="soft grow">Порівнянні продажі, стан і розкриття продавця перевірені до пропозиції. Перший будинок чи п'ятий.</p><span class="arrow">Як проходить купівля</span></a>
<a class="card" href="/uk/sell/"><p class="label">Продаж будинку</p><h3>Правильна ціна, правильна підготовка, один продаж.</h3><p class="soft grow">Ціна на основі реальних продажів, короткий список підготовки, що окупається, і запуск, розрахований на перший тиждень.</p><span class="arrow">Як проходить продаж</span></a>
<a class="card" href="/uk/commercial/"><p class="label">Інвестори та бізнес</p><h3>Будівлі, де цифри сходяться.</h3><p class="soft grow">Багатоквартирні будинки, змішане призначення, торгівля, склади, церкви. Угоди off-market і гнучкі умови.</p><span class="arrow">Комерційна нерухомість</span></a>
</div>
</div></section>

<section class="rule"><div class="wrap section stack lg">
<div class="stack"><p class="chapter">03 · Докази</p><h2>Що кажуть клієнти після закриття угоди.</h2>{NOTE_EN}</div>
{pull("Alena Golovchuk", "He was able to get our offer accepted within 2 days of the home going on market AND drop 15k from the asking price.")}
<div class="grid g3">
{quote("Pavlo Fursyak", "His help didn’t stop after closing. Even after the deal was completed, he continued to check in, answer our questions, and guide us through the next steps.")}
{quote("Heather Sinz", "He is creative, knowledgeable and personable. He helped us find the most house for our money.")}
{quote("Sergey Timoshenko", "Any real estate purchases I make, I’m ALWAYS going with Nazar.")}
</div>
<a class="arrow" href="/reviews/">Усі відгуки</a>
</div></section>

<section class="rule"><div class="wrap section split">
<div class="stack"><p class="chapter">04 · Як ми працюватимемо</p><h2>Від першого дзвінка до ключів: чотири кроки.</h2><p class="soft">Однаково, чи ви купуєте перший будинок, чи чотириквартирний.</p></div>
<ol class="steps">
<li><div><h3>Коротка розмова</h3><p>Чого ви хочете, які терміни і бюджет. Без тиску і без паперів.</p></div></li>
<li><div><h3>Письмовий план</h3><p>Діапазон ціни, міста чи типи об'єктів і як виглядає ваше «так», щоб діяти швидко, коли воно з'явиться.</p></div></li>
<li><div><h3>Робота</h3><p>Покази, ціна, пропозиції і переговори, з розрахунками за кожною порадою.</p></div></li>
<li><div><h3>Закриття і після</h3><p>Інспекція, оцінка і закриття угоди. Після цього я так само на зв'язку щодо підрядників і питань.</p></div></li>
</ol>
</div></section>

<section class="rule"><div class="wrap section split" id="about">
<div><p class="chapter">05 · Хто я</p><h2 style="margin-top:12px">Про Назара</h2><img class="about-photo" src="/images/nazar-orishchin-about.jpg" alt="Назар Оріщин" width="800" height="1200" loading="lazy"></div>
<div class="stack">
<p>Я народився в Україні і переїхав до Міннесоти, коли мені було три. Здобув інженерну освіту і близько п'яти років працював інженером, перш ніж повністю перейти в нерухомість.</p>
<p>Це видно в тому, як я працюю. Я читаю звіт інспектора рядок за рядком, прораховую кожну інвестиційну угоду і називаю цифру прямо. Я також вмію працювати руками, тож можу реально оцінити, що потрібно для ремонту.</p>
<p>Працюю в офісі RE/MAX Results в Eden Prairie у складі Team Steady. Поза роботою я чоловік і тато.</p>
<h3 style="margin-top:16px">Де я працюю найбільше</h3>
<ul class="towns"><li>Chaska</li><li>Chanhassen</li><li>Victoria</li><li>Eden Prairie</li><li>Hopkins</li><li>Savage</li><li>Shakopee</li><li>Burnsville</li><li>Prior Lake</li></ul>
<p class="soft">Інвестиційна та комерційна нерухомість по всій Міннесоті.</p>
</div>
</div></section>

<section class="rule"><div class="wrap section stack lg">
<div class="stack"><p class="chapter">06 · З чого почати</p><h2>Ще не готові телефонувати? Почитайте спершу.</h2><p class="soft">Прості поради, написані на основі реальних угод.</p></div>
<div class="grid g3">{card(by["your-first-step-before-buying-a-home"], "uk")}{card(by["buying-your-first-home-in-minnesota"], "uk")}{card(by["which-investment-properties-make-sense"], "uk")}</div>
<a class="arrow" href="/uk/blog/">Усі поради</a>
</div></section>

{next_step("Почніть із короткої розмови.", "Розкажіть, що плануєте. Ви матимете план, незалежно від того, чи працюватимемо ми разом.", lang="uk")}

{newsletter(lang="uk")}
"""
    page("/uk/", "Назар Оріщин | Україномовний ріелтор у Міннесоті",
         "Україномовний агент з нерухомості в Міннесоті. Купівля, продаж та інвестиції: Chaska, Chanhassen, Eden Prairie і вся Міннесота. Колишній інженер, 100+ угод.",
         home, active="/", lang="uk")

    # ---------- buy ----------
    buy = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Купівля будинку</p><h1>Купіть правильний будинок за правильну ціну.</h1>
<p class="lead">Ваш агент читає розкриття продавця, перевіряє порівнянні продажі і каже, коли варто відмовитися. Перший будинок чи п'ятий, процес однаковий, і я пояснюю кожен крок українською.</p>
<div class="cta"><a class="btn primary" href="{SEARCH}" target="_blank" rel="noopener">Пошук будинків на продаж</a><a class="arrow" href="/book/">Або запишіться на розмову</a></div></div>
<div class="photo"><img src="/images/nazar-smiling.jpg" alt="Назар Оріщин біля вікна" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>Як проходить купівля</h2><p class="soft">Сім кроків по порядку.</p></div>
<ol class="steps">
<li><div><h3>Кредитор і бюджет</h3><p>Отримайте pre-approval, щоб знати свій платіж, а продавці сприймали вашу пропозицію серйозно.</p></div></li>
<li><div><h3>Список</h3><p>До першого показу домовляємося, що обов'язково, які міста і який діапазон ціни.</p></div></li>
<li><div><h3>Покази</h3><p>Я показую вік даху і печі, сліди води і все, що коштуватиме вам грошей пізніше.</p></div></li>
<li><div><h3>Пропозиція</h3><p>Ціна, підкріплена недавніми продажами, і умови з урахуванням конкуренції на будинок.</p></div></li>
<li><div><h3>Інспекція</h3><p>Ділимо звіт на справжні проблеми і звичайне обслуговування, і просимо в продавця те, що важливо.</p></div></li>
<li><div><h3>Оцінка і кредит</h3><p>Я тримаю кредитора, title company і агента продавця в графіку.</p></div></li>
<li><div><h3>Закриття</h3><p>Фінальний огляд, підписи, ключі. Після цього я на зв'язку.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>Що ви отримуєте від інженера</h2>
<div class="grid g3">
<div class="card"><h3>Оцінка стану</h3><p class="soft">Я вмію працювати руками і знаю, що потрібно для ремонту. Ви почуєте реальну вартість, перш ніж закохаєтеся в кухню.</p></div>
<div class="card"><h3>Ціна з обґрунтуванням</h3><p class="soft">Кожна цифра в пропозиції походить із порівнянних продажів, скоригованих на стан, з показаними розрахунками.</p></div>
<div class="card"><h3>Прямі відповіді</h3><p class="soft">Якщо будинок переоцінений або має проблему, я так і скажу, навіть якщо це означає більше показів.</p></div>
</div>
{pull("Pavlo Fursyak", "From day one, Nazar made everything feel simple, organized, and stress-free. He patiently answered every question, explained every step, and made sure we always knew what to expect.")}
<a class="arrow" href="/uk/blog/buying-your-first-home-in-minnesota/">Читати: купівля будинку від початку до кінця</a>
</div></section>
{next_step("Знайдімо ваш будинок.", "Коротка розмова, щоб визначити бюджет, міста і обов'язкові вимоги. Потім я надсилатиму вам будинки в день їхньої появи.", lang="uk")}
"""
    page("/uk/buy/", "Купівля будинку в Міннесоті українською | Назар Оріщин",
         "Купівля будинку в Chaska, Chanhassen, Eden Prairie та західних передмістях з україномовним агентом, який перевіряє ціни, стан і документи до пропозиції.",
         buy, active="/buy/", lang="uk")

    # ---------- sell ----------
    sell = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Продаж будинку</p><h1>Правильна ціна, правильна підготовка, один продаж.</h1>
<p class="lead">Будинки, що застоюються, дешевшають. Тому ми виходимо на ринок за ціною, з якою ринок погодиться, з будинком, готовим до фото, і я тримаю вас у курсі до закриття.</p>
<div><a class="btn primary" href="/book/">Дізнайтеся ціну: 15-хвилинна розмова</a></div></div>
<div class="photo"><img src="/images/nazar-laughing.jpg" alt="Назар Оріщин усміхається" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>Як проходить продаж</h2><p class="soft">Шість кроків від першого огляду до закриття.</p></div>
<ol class="steps">
<li><div><h3>Огляд</h3><p>Я дивлюся будинок, питаю про оновлення і дізнаюся ваші терміни.</p></div></li>
<li><div><h3>Ціна</h3><p>Ви отримуєте недавні продажі, поточну конкуренцію і рекомендовану ціну з обґрунтуванням.</p></div></li>
<li><div><h3>Підготовка</h3><p>Короткий список ремонтів, що окупаються. Ті, що не окупаються, пропускаю.</p></div></li>
<li><div><h3>Фото і запуск</h3><p>Професійні фото, опис, написаний саме про ваш будинок, і запуск у час, коли буде найбільше показів.</p></div></li>
<li><div><h3>Пропозиції</h3><p>Я розкладаю кожну пропозицію поруч: ціна, фінансування, умови і ризики.</p></div></li>
<li><div><h3>Від інспекції до закриття</h3><p>Веду переговори щодо ремонтів і тримаю title company, кредитора і агента покупця в русі.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>Продаж і купівля одночасно</h2>
<p class="lead">Більшості продавців теж потрібно десь жити. Я планую обидві угоди разом, щоб вам не довелося платити за два будинки чи жити серед коробок.</p>
{pull("Heather Sinz", "Nazar went above and beyond for my husband and I, from start to finish, helping us balance selling and buying at the same time.")}
<a class="arrow" href="/uk/blog/selling-your-home-what-the-first-30-days-look-like/">Читати: 30 днів до виставлення на ринок</a>
</div></section>
{next_step("Хочете знати ціну свого будинку?", "Я подивлюся будинок особисто і назву діапазон ціни з обґрунтуванням. Без зобов'язань.", lang="uk")}
"""
    page("/uk/sell/", "Продаж будинку в Міннесоті українською | Назар Оріщин",
         "Продаж будинку в Chaska, Chanhassen, Eden Prairie та західних передмістях: ціна на основі ринку, короткий список підготовки і зрозумілі оновлення до закриття.",
         sell, active="/sell/", lang="uk")

    # ---------- commercial ----------
    com = f"""
<div class="wrap page-hero split">
<div class="stack lg"><p class="label">Інвестори та комерційна нерухомість</p><h1>Багатоквартирні та комерційні будівлі, де цифри сходяться.</h1>
<p class="lead">Я знаходжу, прораховую і закриваю інвестиційні об'єкти по всій Міннесоті, як на ринку, так і поза ним. Спершу інженер, потім агент: якщо цифри не сходяться, я скажу це до того, як ви витратите гроші на перевірки.</p>
<div><a class="btn primary" href="mailto:Nazar@ts-re.com?subject=Об'єкт%20для%20аналізу">Надішліть мені об'єкт для аналізу</a></div></div>
<div class="photo"><img src="/images/nazar-window.jpg" alt="Назар Оріщин дивиться у вікно" width="800" height="1200"></div>
</div>
<section class="rule"><div class="wrap section stack lg">
<h2>Типи об'єктів</h2>
<ul class="tags"><li>Багатоквартирні будинки</li><li>Змішане призначення</li><li>Роздрібна торгівля</li><li>Торгові центри</li><li>Склади</li><li>Церкви</li><li>Автосалони</li><li>Спеціальне призначення</li></ul>
</div></section>
<section class="rule"><div class="wrap section stack lg">
<h2>Як я працюю</h2>
<div class="grid g3">
<div class="card"><p class="label">Пошук</p><h3>Спершу off-market</h3><p class="soft">Багато будівель продаються без оголошення. Я досліджую власників, телефоную і приношу вам ті, що варті уваги.</p></div>
<div class="card"><p class="label">Аналіз</p><h3>Цифри з нуля</h3><p class="soft">Список орендарів, реальні витрати, податки і скільки залишилося даху та інженерним системам. Потім перевіряю цифри на міцність.</p></div>
<div class="card"><p class="label">Структура</p><h3>Гнучкі умови</h3><p class="soft">Seller carry, contract for deed і довше закриття, коли одного банківського кредиту недостатньо.</p></div>
</div>
{pull("jarred knapp", "When unexpected issues came up (as they always do in real estate), he never got rattled—he calmly found solutions and kept everything moving forward.")}
</div></section>
<section class="rule"><div class="wrap section split">
<div class="stack"><h2>З ким я працюю</h2></div>
<ol class="steps">
<li><div><h3>Інвестори</h3><p>Перша орендна нерухомість чи портфель, що зростає. Скажіть, що купуєте, і я надсилатиму те, що підходить.</p></div></li>
<li><div><h3>Власники бізнесу</h3><p>Купівля власної будівлі: майстерні, автосалони, склади, церкви.</p></div></li>
<li><div><h3>Власники, які думають про продаж</h3><p>Тиха розмова про вартість і варіанти, без таблички і без тиску.</p></div></li>
</ol>
</div></section>
<section class="rule"><div class="wrap section split faq">
<h2>Часті запитання</h2>
<div>
<details><summary>Де в Міннесоті ви працюєте?</summary><p>З інвестиційною та комерційною нерухомістю працюю по всьому штату. Більшість роботи зосереджена в агломерації Twin Cities і містах за кілька годин від неї.</p></details>
<details><summary>Що таке угода off-market?</summary><p>Продаж без публічного оголошення. Власника і покупця знайомлять напряму, зазвичай через агента, який провів дослідження і зателефонував.</p></details>
<details><summary>Що таке гнучкі умови?</summary><p>Усе, окрім готівки чи стандартного банківського кредиту. Найпоширеніші з них: seller carry і contract for deed, коли продавець фінансує частину або всю ціну. <a href="/uk/blog/contract-for-deed-minnesota/">Ось як працює contract for deed.</a></p></details>
<details><summary>Ви працюєте з інвесторами-початківцями?</summary><p>Так. Починаємо з того, скільки ви можете вкласти і яка дохідність вам потрібна, а потім дивимося на реальні будівлі під ці цифри.</p></details>
<details><summary>У мене є будівля. Можемо поговорити без виставлення на продаж?</summary><p>Так. Я назву діапазон вартості і поясню варіанти. Нічого не стане публічним, якщо ви цього не вирішите.</p></details>
</div>
</div></section>
{next_step("Маєте будівлю чи угоду на прикметі?", "Надішліть адресу і все, що знаєте, . Я скажу, чи сходяться цифри.", lang="uk")}
"""
    page("/uk/commercial/", "Комерційна та багатоквартирна нерухомість у Міннесоті | Назар Оріщин",
         "Багатоквартирні будинки, змішане призначення, торгівля, склади, церкви та об'єкти спеціального призначення в Міннесоті. Угоди off-market, аналіз і гнучкі умови. Українською.",
         com, active="/commercial/", lang="uk")

    # ---------- blog index ----------
    start = [p for p in POSTS if p["cat"] == "Start here"]
    rest = [p for p in POSTS if p["cat"] != "Start here"]
    blog = f"""
<div class="wrap page-hero stack lg"><p class="label">Поради</p><h1>Прості поради про купівлю, продаж та інвестиції в Міннесоті.</h1>
<p class="lead">Написані на основі угод, які я провів. Якщо ви тільки починаєте, прочитайте спершу перші три.</p></div>
<section class="rule"><div class="wrap section stack lg"><p class="chapter">З чого почати</p><div class="grid g3">{"".join(card(p, "uk") for p in start)}</div></div></section>
<section class="rule"><div class="wrap section stack lg"><p class="chapter">Більше порад</p><div class="grid g3">{"".join(card(p, "uk") for p in rest)}</div></div></section>
{next_step(lang="uk")}
{newsletter(lang="uk")}
"""
    page("/uk/blog/", "Поради з нерухомості в Міннесоті українською | Назар Оріщин",
         "Практичні поради українською про купівлю, продаж та інвестиції в нерухомість у Міннесоті: інспекція, contract for deed, угоди off-market та інше.",
         blog, active="/blog/", lang="uk")

    # ---------- posts ----------
    for p in POSTS:
        u = p["uk"]
        path = f'/uk/blog/{p["slug"]}/'
        pld = json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": u["title"], "inLanguage": "uk",
                          "datePublished": p["date"], "author": {"@type": "Person", "name": "Nazar Orishchin", "url": SITE + "/uk/"},
                          "mainEntityOfPage": SITE + path}, ensure_ascii=False)
        related = [q for q in POSTS if q is not p and q["cat"] == p["cat"]][:2] or [q for q in POSTS if q is not p][:2]
        body = f"""
<article class="article">
<a class="arrow back" href="/uk/blog/" style="padding:0">Усі поради</a>
<p class="post-meta" style="margin-top:20px">{CAT_UK[p["cat"]]} · <time datetime="{p["date"]}">{uk_date(p["date"])}</time> · {u["mins"]} хв читання</p>
<h1>{u["title"]}</h1>
<p class="lead">{u["teaser"]}</p>
{u["body"]}
<div class="byline"><img src="/images/nazar-orishchin-about.jpg" alt="" width="64" height="64" loading="lazy"><p><b>Назар Оріщин</b><br>Агент з нерухомості, RE/MAX Results, Team Steady. <a href="/book/">Запис на розмову</a></p></div>
</article>
<section class="rule"><div class="wrap section stack lg"><p class="chapter">Читайте також</p><div class="grid g2">{"".join(card(q, "uk") for q in related)}</div></div></section>
"""
        page(path, f'{u["title"]} | Назар Оріщин', u["desc"], body, active="/blog/", lang="uk",
             extra_head=f'<script type="application/ld+json">{pld}</script>\n')
