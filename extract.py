#!/usr/bin/env python
import argparse
import json
import sys
from datetime import datetime

import pandas as pd


def converter(value):
    if pd.isna(value):
        return None
    elif isinstance(value, pd.Period):
        return str(value)
    else:
        value

def main(years_since_death=80):
    authors = pd.read_csv("authors.csv")
    authors["dod"] = pd.PeriodIndex([
        pd.Period(d, freq="D") for d in authors.dod
    ])
    year = datetime.utcnow().year - years_since_death
    public_domain_authors = authors.query(
        f"not dod.isnull() and dod.dt.year < {year}"
    ).infile.values.tolist()
    poems = json.load(open("poesias_corpora.json"))
    public_domain_works_raw = list(filter(
        lambda d: d["author"] in public_domain_authors, poems.values()
    ))
    authors_data = {a["infile"]: a for a in authors.to_dict(orient="records")}
    public_domain_works = []
    for work in public_domain_works_raw:
        author = authors_data[work["author"]].copy()
        author["name"] = author["author"]
        del author["author"]
        del author["birth_date"]
        del author["death_date"]
        del author["century"]
        del author["infile"]
        work.update({f"author_{k}": v for k, v in author.items()})
        del work["century"]
        public_domain_works.append(work)
    public_domain_works_json = json.dumps(
        public_domain_works, indent=4, default=converter)
    print(public_domain_works_json, file=sys.stdout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Generates a public domain corpus in JSON")
    parser.add_argument("-y", "--years", type=int, default=80,
                        help="Number of years since death of authors "
                             "a work is considered to be public domain")
    args = parser.parse_args()
    main(args.years)
