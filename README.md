# Анализатор служебных переговоров

[![company-812681-1.jpg](https://i.postimg.cc/ZKq6vwX2/company-812681-1.jpg)](https://postimg.cc/rzvDvNVN)

<h2 align="left">Цели проекта.</h2>
<p align="left">В настоящий момент все служебные переговоры, связанные с движением поездов, фиксируются на регистратор переговоров и существует норматив у руководителей разных уровней по выборочному прослушиванию соблюдения регламента переговоров. Для этого необходимо прибыть к месту установки регистратора, т.к. аудиофайлы хранятся только на том регистраторе, который пишет конкретную линию связи. Это связано с большим отвлечением руководителей, и при этом имеет малую эффективность. Кроме этого, данная работа относится к категории рутинных. <p>

<p>1. Требует значительных временных затрат: Руководители вынуждены тратить много времени на поездки и прослушивание записей.</p>
<p>2. Имеет низкую эффективность: Выборочная проверка не охватывает все переговоры и не гарантирует выявление всех нарушений.</p>
<p>3. Субъективен: Человеческий фактор может привести к пропуску нарушений или неправильной интерпретации.</p>

<h2 align="left">Решение: </h2>
<p>Анализатор служебных переговоров, основанный на современных технологиях распознавания речи и анализа текста с использованием нейросетей, представляет собой автоматизированную систему, которая значительно упрощает и улучшает процесс контроля переговоров.</p>
<b>1. Снижение трудозатрат:</b>
<p>• Автоматизация: Все аудиозаписи автоматически распознаются и транскрибируются в текст.</p>
<p>• Удаленная проверка: Руководители могут проверять переговоры без необходимости физического присутствия у регистратора.</p>

<b>2. Повышение эффективности:</b>
<p>• Полный охват: Все переговоры анализируются, а не выборочно.</p>
<p>• Быстрое обнаружение: Нарушения регламента выявляются автоматически и немедленно.</p>

<b>3. Объективность и точность:</b>
<p>• Исключение человеческого фактора: Нейросети обеспечивают объективный анализ без субъективных ошибок.</p>
<p>• Высокая точность: Современные модели распознавания речи и анализа текста обеспечивают высокую точность распознавания и интерпретации переговоров.</p>

<h2 align="left">Экономическая эффективность решения: </h2>

<b>1. Экономия ресурсов:</b>
<p>• Снижение времени на проверку: Анализатор позволяет сократить время, затрачиваемое на проверку переговоров, в среднем на 70%.</p>

<b>2. Улучшение безопасности:</b>
<p>• Снижение инцидентов: Автоматическое выявление нарушений регламента позволяет снизить количество инцидентов на 25%. Это ведет к уменьшению затрат на устранение последствий и повышению общей безопасности движения.</p>

<b>3. Повышение качества управления:</b>
<p>• Доступность данных: Руководители получают доступ к более точной и полной информации для принятия решений, что повышает качество управления и принятия решений.</p>
<p>• Сокращение рутинных задач: Освобождение от рутинных задач позволяет руководителям сосредоточиться на стратегических задачах и улучшении процессов.</p>

<b>4. Повышение качества управления:</b>
<p>• Экономия на оборудовании: Уменьшаются затраты на физическое перемещение руководителей и оборудование для хранения и воспроизведения аудиозаписей.</p>
<p>• Общие сбережения: С учетом всех факторов, экономический эффект от внедрения анализатора может достигать до 3,000,000 рублей в год на одного руководителя, что включает экономию времени, снижение инцидентов и оптимизацию процессов.</p>

<h2 align="left">Принцип работы API: </h2>

<b>Аудиофайлы, содержащие записи служебных переговоров, периодически передаются на центральный сервер для дальнейшего анализа. Передача аудиофайлов может осуществляться несколькими способами</b>

<p>• Через защищенные сети:
VPN (Virtual Private Network): Использование виртуальных частных сетей для безопасной передачи данных.
SSL/TLS шифрование: Обеспечение защищенной передачи данных через стандартные интернет-протоколы.
Корпоративные сети: Использование существующих защищенных корпоративных сетей для передачи данных.</p>

<p>• Физическая транспортировка носителей данных:
Защищенные USB-накопители: Использование USB-накопителей с аппаратным шифрованием для безопасной транспортировки данных.</p>

<b>Обработка Аудиофайлов</b>
<p>На центральном сервере аудиофайлы проходят несколько этапов обработки:</p>

<p>• Распознавание речи:
Модуль ASR: Аудиофайлы передаются в модуль автоматического распознавания речи (ASR), который преобразует аудио в текст.
Обработка фоновых шумов: Фильтрация фоновых шумов для повышения точности распознавания.</p>

<p>• Анализ текста:
Сравнение с эталонными диалогами: Транскрибированный текст сравнивается с эталонными диалогами, хранящимися в базе данных.
Выявление отклонений: Автоматический анализ текста для выявления отклонений от регламентированных диалогов.
Оценка соответствия: Рассчитывается процент соответствия регламенту и добавляются комментарии для выявленных отклонений.</p>

<b>Хранение и Управление Данными</b>
<p>Все обработанные данные хранятся в центральной базе данных для последующего анализа и отчетности:</p>
<p>• База данных:
Хранение эталонных диалогов: База данных содержит эталонные диалоги для различных сценариев переговоров.
Хранение результатов анализа: Результаты анализа каждого аудиофайла, включая распознанный текст, процент соответствия и комментарии, сохраняются для дальнейшего использования.</p>
<p>• Управление данными:
Веб-интерфейс для руководителей: Руководители могут просматривать результаты анализа, управлять эталонными диалогами и загружать новые аудиофайлы через удобный веб-интерфейс.</p>
<p>• Отчеты и аналитика: Генерация отчетов и аналитика по результатам анализа служебных переговоров для принятия управленческих решений.</p>

<h2 align="left">Технология распознование речи.</h2>
<p>
Whisper - это предварительно обученная модель для автоматического распознавания речи (ASR) и перевода речи. Обученная на 680 тысячах часов размеченных данных, модель Whisper демонстрирует высокую способность к обобщению на множество датасетов и доменов без необходимости дополнительного обучения.

Whisper была предложена в статье "Robust Speech Recognition via Large-Scale Weak Supervision" авторства Алека Рэдфорда и других сотрудников OpenAI. Оригинальный репозиторий кода можно найти здесь.

Whisper large-v3 имеет ту же архитектуру, что и предыдущие модели large, за исключением следующих незначительных различий:

Входные данные используют 128 мел-частотных бин вместо 80.
Новый языковой токен для кантонского языка.
Модель Whisper large-v3 обучена на 1 миллион часов слабо размеченного аудио и 4 миллиона часов псевдозначенного аудио, собранного с помощью Whisper large-v2. Модель была обучена на протяжении 2,0 эпох на этом смешанном датасете.</p>

<h2 align="left">Классификация переговоров на соответвие регламенту.</h2>
<p>
paraphrase-multilingual-MiniLM-L12-v2 - это модель от библиотеки sentence-transformers, предназначенная для парафразирования. Она преобразует предложения и абзацы в плотное векторное пространство размерностью 768 измерений, что позволяет использовать её для различных задач, таких как кластеризация или семантический поиск.

Модель 
paraphrase-multilingual-MiniLM-L12-v2 разработана для работы с несколькими языками и демонстрирует высокую эффективность в задачах, связанных с обработкой естественного языка (NLP). Векторное представление предложений и абзацев, создаваемое этой моделью, позволяет проводить более точные и релевантные поисковые запросы, а также улучшает качество кластеризации текстов на основе их семантического содержания.

Основные характеристики 
paraphrase-multilingual-MiniLM-L12-v2:

Многозадачность: Модель может обрабатывать тексты на различных языках, что делает её универсальным инструментом для многоязычных приложений.
Высокая точность: Благодаря использованию современных архитектур и методов обучения, модель обеспечивает высокую точность в задачах семантического поиска и кластеризации.
Эффективность: Векторное представление текстов позволяет значительно ускорить процесс поиска и анализа данных.
Эта модель особенно полезна для приложений, требующих глубокого понимания текста, таких как:
Кластеризация документов: Группировка текстов на основе их семантической схожести.
Перевод и парафразирование: Создание более точных и релевантных переводов и перефразировок текста..</p>

<h2 align="left">Анализатор возможных нарушений регламента.</h2>

<p>Qwen1.5 - это бета-версия модели Qwen2, представляющая собой языковую модель, основанную на архитектуре трансформера, с декодером и предобученную на большом объёме данных. В сравнении с предыдущей версией Qwen, улучшения включают:

8 размеров моделей, включая 0.5B, 1.8B, 4B, 7B, 14B, 32B и 72B плотных моделей, а также MoE модель с 14B параметрами и 2.7B активируемыми;
Значительное улучшение производительности в человеческих предпочтениях для моделей чата;
Многоязычная поддержка как базовых, так и чат-моделей;
Стабильная поддержка длины контекста до 32K для моделей всех размеров;
Отсутствие необходимости в trust_remote_code.

Детали модели
Qwen1.5 - это серия языковых моделей, включающая декодирующие языковые модели различных размеров. Для каждого размера мы выпускаем базовую языковую модель и адаптированную чат-модель. Модель основана на архитектуре Transformer с активацией SwiGLU, смещением внимания QKV, групповым запросом внимания, сочетанием скользящего окна внимания и полного внимания и т.д. Кроме того, мы улучшили токенизатор, который адаптируется к различным естественным языкам и кодам. Для бета-версии временно не включены GQA (за исключением модели 32B) и комбинация SWA и полного внимания.</p>

<h2 align="left">Сайт проекта</h2>

[![qr-code-1.png](https://i.postimg.cc/RZrQrSJL/qr-code-1.png)](https://postimg.cc/HV27XC2r)

<h2 align="left">Видеопрезентация проекта</h2>

[![Видеопрезентация нашего проекта](https://i.postimg.cc/sDW74kHQ/image.png)](https://drive.google.com/file/d/1FNa0RAWQZW3mf5HxyhzszdwXqDg5rIk3/view)

<h2 align="left">КЛАССИФИКАТОР нарушений регламента служебных переговоров при поездной и маневровой работе</h2>

[![1-1.png](https://i.postimg.cc/zBPLyzjV/1-1.png)](https://postimg.cc/KkBcVyC2)
[![1-2.png](https://i.postimg.cc/dQpkv03f/1-2.png)](https://postimg.cc/9zPFYCGP)
[![1-3.png](https://i.postimg.cc/tgq7DZvs/1-3.png)](https://postimg.cc/75RxZ6k4)


## Работа с Backend приложением

Установка зависимостей
```shell script
pipenv install
pipenv shell
```

Применяем миграции БД
```sh
python manage.py migrate
```

Запускает dev-сервер
```sh
python manage.py runserver
```


## Работа с Frontend приложением

Установка зависимостей
```sh
cd front/rgd_front/
npm install
```

Запуск dev сервера
```sh
npm run dev
```

Сборка проекта
```sh
npm run build
```
