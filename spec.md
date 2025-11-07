# problems

## Mongo TUI (data exploration)

🎗️ serde.md > JSON > in databases
🗄️ `OLTP.md` > Mongo > workflow

## wtfk

🗄️ `projects/active/wtfk`

https://claude.ai/chat/f894227a-6c96-4680-b26e-2d634af1a313

I want to hook up an LLM to Mongo to cruise around collections, do some sampling, and figure out the FKs and how everything hooks together.

* List all tables
* Sample data from each
* Analyze column names, data types, and values
* Infer foreign key relationships
* Build a schema graph

Assuming we'll use these libs, I've added them (managing the project with Poetry):

* anthropic
* pymongo
* Click

I'd like output to be:

* Markdown
* d2 documents (see erd-example.d2)

Let's start with something straightforward: connect to db given URL string and list 5 databases.

## Mongo TUI (search)

* `uuid_search.py`
