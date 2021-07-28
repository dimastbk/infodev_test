from collections import Counter


def count_letters():
    some_text = (
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
        ' Alias aut commodi consequuntur dolorum, '
        'incidunt neque numquam perferendis repellat sapiente tempora, '
        'vitae voluptatibus. Earum error fugit '
        'harum illum temporibus vel vero.'
    )

    # Приводим в нижний регистр и очищаем от небуквенных символов
    counter = Counter(s for s in some_text.lower() if s.isalpha())
    print(f'max = {counter.most_common(3)}')
    print(f'min = {counter.most_common(None)[-3:]}')
