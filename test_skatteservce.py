import json
import unittest
import json

from app import get_all_skattemeldinger, get_skattemelding

class TestEvalute(unittest.TestCase):
        
    def test_get_skattemelding(self):
        test_data = {
            "personidentifikator": "03839199405",
            "inntektsaar": "2019",
            "skjermet": False,
            "sumSaerfradrag": 123,
            "tolvdeler": 12,
            "skatteklasse": "6",
            "nettoformue": 1234500,
            "nettoinntekt": 504321,
            "utlignetSkatt": 654321,
            "formueskattStat": 5489,
            "formueskattKommune": 1111,
            "kreditfradragFormue": 852,
            "kreditfradragInntekt": 5698,
            "alminneligInntektFoerSaerfradrag": 4587,
            "skatteoppgjoersdato": "2020-04-07",
            "skatteregnskapskommune": "7015",
            "svalbardLoennLoennstrekkordningen": 54331,
            "svalbardPensjonLoennstrekkordningen": 7894,
            "svalbardLoennUtenTrygdeavgiftLoennstrekkordningen": 457,
            "svalbardNettoformue": 7896,
            "svalbardNettoinntekt": 45870,
            "svalbardUtlignetSkatt": 4258,
            "svalbardUfoeretrygdLoennstrekkordningen": 7412,
            "svalbardSkattOrdinaerAlminneligInntekt": 89547,
            "svalbardFormueskatt": 7863,
            "svalbardFastsattSkattEtterLoennstrekkordningen": 478,
            "svalbardSkatteregnskapskommune": "2222"
        }

        skattemelding = json.loads(get_skattemelding(inntektsaar="2019", personidentifikator="03839199405"))

        self.assertDictEqual(skattemelding, test_data, "Skattemelding is not good")
        

    def test_all_skattemelding(self):
        test_data = json.load(open('skattemeldinger.json'))
        all_skattemelding = get_all_skattemeldinger()
        self.assertDictEqual(all_skattemelding, test_data, "Skattemessages is wrong")

if __name__ == '__main__':
    unittest.main()