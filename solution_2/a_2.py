import json
import pandas as pd


class Population:

    def __init__(self):
        self.students = None
        self.undergraduates = None
        self.postgraduates = None

    def __repr__(self):
        return f'{self.__dict__}'

    def toDict(self):
        return dict(
            students=self.students,
            undergraduates=self.undergraduates,
            postgraduates=self.postgraduates
        )

    def toJson(self):
        return json.dumps(self.toDict())


def producer(url: str) -> [Population]:
    dfs = pd.read_html(url)

    pops = []

    for df in dfs:
        df = df.T
        df = df.rename(columns=df.iloc[0])

        try:
            df = df.drop(0)
        except:
            pass

        p = Population()

        for col in df.columns:

            try:

                if 'students'.lower() == f'{col}'.lower():
                    p.students = df.loc[:, col].apply(
                        lambda x: x.split(' ')).apply(
                        lambda x: x[0]
                    ).to_string(index=False)
                if 'undergraduates'.lower() == f'{col}'.lower():
                    p.undergraduates = df.loc[:, col].apply(
                        lambda x: x.split(' ')).apply(
                        lambda x: x[0]
                    ).to_string(index=False)
                if 'postgraduates'.lower() == f'{col}'.lower():
                    p.postgraduates = df.loc[:, col].apply(
                        lambda x: x.split(' ')).apply(
                        lambda x: x[0]
                    ).to_string(index=False)
            except:
                pass

        if p.students and p.undergraduates and p.postgraduates:
            pops.append(p)

    return pops


def main(urls: list) -> [(str, [Population])]:
    results = []
    for url in urls:
        results.append((url, producer(url)))

    return results


if __name__ == "__main__":
    urls = [
        'https://en.wikipedia.org/wiki/Michigan_State_University',
        'https://en.wikipedia.org/wiki/University_of_Virginia'
    ]

    answers = main(urls)

    for answer in answers:
        url, population = answer
        print(url)

        for p in population:
            print(p.toJson())
