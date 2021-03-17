import re

questions = []

with open('.testing/questions_test_inp.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        questions.append(line)

questions_clean = []

pattern = re.compile(r"\d*\.\s")

for question in questions:
    questions_clean.append(pattern.sub("", question))

for question in questions_clean:
    with open(".testing/questions.txt", "a", encoding='utf-8') as f:
        f.write(question + "\n")