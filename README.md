Siyasi Partiler Veritabanı
--------------------------

TC tarihi boyunca parti ve örgütlerin birleşme/bölünme/kapanma bilgilerini içerir.

CSV, JSON ve GML formatlarındadır.

Google spreadsheets API üzerinden de erişebilirsiniz.

URL: https://docs.google.com/spreadsheets/d/1hYoKyzS-NIkVag3YRb59BWiWCtiPtN24FaC8EWMml7k/

Google Spreadsheets API'ın jQuery ile kullanımına bir örnek:

```javascript
var readFromGoogleDocs = function (spreadsheetId, callback) {

    var url = ("https://spreadsheets.google.com/feeds/list/"+ spreadsheetId
        + "/od6/public/values?alt=json-in-script&callback=?");

    var columnMapping = {
        "name": "name",
        "abbreviation": "abbreviation",
        "leader": "leader",
        "founded": "founded",
        "dissolved": "dissolved",
        "reasonofdissolution": "reasonOfDissolution",
        "descendantof": "descendantOf",
        "ancestorof": "ancestorOf",
        "politicalposition": "politicalPosition",
        "ideology": "ideology",
        "source": "source",
        "publications": "publications",
        "notes": "notes"
    };

    var iterableColumns = ["leader", "founded", "dissolved", "descendantof",
                           "ancestorof", "ideology", "source", "notes", "publications"];

    var numericColumns = ["founded", "dissolved"];

    $.getJSON(url, function (response) {
        var result = [];

        $(response.feed.entry).each(function (index, entry) {
            var bundle = {};
            for (var columnName in columnMapping) {
                var cell = entry["gsx$" + columnName];

                if (!cell) {
                    continue;
                }

                var node = cell["$t"].trim();

                if (iterableColumns.indexOf(columnName) > -1) {
                    if (node) {
                        node = node.split(",").map(function (str) {
                            return str.trim();
                        })
                    } else {
                        node = [];
                    }
                }

                if (numericColumns.indexOf(columnName) > -1) {
                    if (iterableColumns.indexOf(columnName) > -1) {
                        node = node.map(function (item) {
                            var value = parseInt(item);
                            return isNaN(value) ? Infinity : value;
                        });
                    } else {
                        node = parseInt(node);
                    }
                }

                bundle[columnMapping[columnName]] = node;
            }

            result.push(bundle);

        });

        callback(result);

    });

}

```

Gephi üzerinde örnek bir görselleştirme:

![Sol](https://scontent-b-ams.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/10698690_10152734087742487_8516757143911846760_n.jpg?oh=c00c0104e753f2e5b1ca587dae2fa44d&oe=54C9DDA7 "Sol")

