import numpy as np
import os

id_to_char = {}
char_to_id = {}

def _update_vocab(txt):
    chars = list(txt)

    for i, char in enumerate(chars):
        if char not in char_to_id:
            tmp_id = len(char_to_id)
            char_to_id[char] = tmp_id
            id_to_char[tmp_id] = char


def load_data(file_name='addition.txt', seed=1984):
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name

    if not os.path.exists(file_path):
        print('No file: %s' % file_name)
        return None

    questions, answers = [], []

    for line in open(file_path, 'r'):
        idx = line.find('_')
        questions.append(line[:idx])
        answers.append(line[idx + 1:-1])

    # 어휘 사전 생성
    for i in range(len(questions)):
        q, a = questions[i], answers[i]
        _update_vocab(q)
        _update_vocab(a)

    # 시퀀스 길이를 계산
    max_q_len = max(len(q) for q in questions)
    max_a_len = max(len(a) for a in answers)

    # 길이가 다른 시퀀스를 처리하는 방법
    x = []
    t = []

    for i, sentence in enumerate(questions):
        x.append([char_to_id[c] for c in sentence] + [0] * (max_q_len - len(sentence)))  # 패딩 추가
    for i, sentence in enumerate(answers):
        t.append([char_to_id[c] for c in sentence] + [0] * (max_a_len - len(sentence)))  # 패딩 추가

    x = np.array(x)
    t = np.array(t)

    # 뒤섞기
    indices = np.arange(len(x))
    if seed is not None:
        np.random.seed(seed)
    np.random.shuffle(indices)
    x = x[indices]
    t = t[indices]

    # 검증 데이터셋으로 10% 할당
    split_at = len(x) - len(x) // 10
    (x_train, x_test) = x[:split_at], x[split_at:]
    (t_train, t_test) = t[:split_at], t[split_at:]

    return (x_train, t_train), (x_test, t_test)


def get_vocab():
    return char_to_id, id_to_char
