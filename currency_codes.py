"""When looking at the ExchangeRate-API, it needed the ISO4217 code of the country to find the exchange rate.
Because the user is able to input their destination, I needed a way to turn that into the ISO3217 code.
I couldn't find an API that did that, so I wrote this function to work it out."""

def iso_code_finder(placename):
    iso_code = [{"code": "AED", "currency-name": "UAE Dirham", "country": "United Arab Emirates"},
                  {"code": "AFN", "currency-name": "Afghan Afghani", "country": "Afghanistan"},
                  {"code": "ALL", "currency-name": "Albanian Lek", "country": "Albania"},
                  {"code": "AMD", "currency-name": "Armenian Dram", "country": "Armenia"},
                  {"code": "ANG", "currency-name": "Netherlands Antillian Guilder", "country": "Netherlands Antilles"},
                  {"code": "AOA", "currency-name": "Angolan Kwanza", "country": "Angola"},
                  {"code": "ARS", "currency-name":	"Argentine Peso", "country": "Argentina"},
                  {"code": "AUD", "currency-name":	"Australian Dollar", "country": "Australia"},
                  {"code": "AWG", "currency-name":	"Aruban Florin", "country": "Aruba"},
                  {"code": "AZN", "currency-name":	"Azerbaijani Manat", "country": "Azerbaijan"},
                  {"code": "BAM", "currency-name":	"Bosnia and Herzegovina Mark", "country": "Bosnia and Herzegovina"},
                  {"code": "BBD", "currency-name":	"Barbados Dollar", "country": "Barbados"},
                  {"code": "BDT", "currency-name":	"Bangladeshi Taka", "country": "Bangladesh"},
                  {"code": "BGN", "currency-name":	"Bulgarian Lev", "country": "Bulgaria"},
                  {"code": "BHD", "currency-name":	"Bahraini Dinar", "country": "Bahrain"},
                  {"code": "BIF", "currency-name":	"Burundian Franc", "country": "Burundi"},
                  {"code": "BMD", "currency-name":	"Bermudian Dollar", "country": "Bermuda"},
                  {"code": "BND", "currency-name":	"Brunei Dollar", "country": "Brunei"},
                  {"code": "BOB", "currency-name":	"Bolivian Boliviano", "country": "Bolivia"},
                  {"code": "BRL", "currency-name":	"Brazilian Real", "country": "Brazil"},
                  {"code": "BSD", "currency-name":	"Bahamian Dollar", "country": "Bahamas"},
                  {"code": "BTN", "currency-name":	"Bhutanese Ngultrum", "country": "Bhutan"},
                  {"code": "BWP", "currency-name":	"Botswana Pula", "country": "Botswana"},
                  {"code": "BYN", "currency-name":	"Belarusian Ruble", "country": "Belarus"},
                  {"code": "BZD", "currency-name":	"Belize Dollar", "country": "Belize"},
                  {"code": "CAD", "currency-name":	"Canadian Dollar", "country": "Canada"},
                  {"code": "CDF", "currency-name":	"Congolese Franc", "country": "Democratic Republic of the Congo"},
                  {"code": "CHF", "currency-name":	"Swiss Franc", "country": "Switzerland"},
                  {"code": "CLP", "currency-name":	"Chilean Peso", "country": "Chile"},
                  {"code": "CNY", "currency-name":	"Chinese Renminbi", "country": "China"},
                  {"code": "COP", "currency-name":	"Colombian Peso", "country": "Colombia"},
                  {"code": "CRC", "currency-name":	"Costa Rican Colon", "country": "Costa Rica"},
                  {"code": "CUP", "currency-name":	"Cuban Peso", "country": "Cuba"},
                  {"code": "CVE", "currency-name":	"Cape Verdean Escudo", "country": "Cape Verde"},
                  {"code": "CZK", "currency-name":	"Czech Koruna", "country": "Czech Republic"},
                  {"code": "DJF", "currency-name":	"Djiboutian Franc", "country": "Djibouti"},
                  {"code": "DKK", "currency-name":	"Danish Krone", "country": "Denmark"},
                  {"code": "DOP", "currency-name":	"Dominican Peso", "country": "Dominican Republic"},
                  {"code": "DZD", "currency-name":	"Algerian Dinar", "country": "Algeria"},
                  {"code": "EGP", "currency-name":	"Egyptian Pound", "country": "Egypt"},
                  {"code": "ERN", "currency-name":	"Eritrean Nakfa", "country": "Eritrea"},
                  {"code": "ETB", "currency-name":	"Ethiopian Birr", "country": "Ethiopia"},
                  {"code": "EUR", "currency-name":	"Euro", "country": "European Union"},
                  {"code": "FJD", "currency-name":	"Fiji Dollar", "country": "Fiji"},
                  {"code": "FKP", "currency-name":	"Falkland Islands Pound", "country": "Falkland Islands"},
                  {"code": "FOK", "currency-name":	"Faroese Króna", "country": "Faroe Islands"},
                  {"code": "GBP", "currency-name":	"Pound Sterling", "country": "United Kingdom"},
                  {"code": "GEL", "currency-name":	"Georgian Lari", "country": "Georgia"},
                  {"code": "GGP", "currency-name":	"Guernsey Pound", "country": "Guernsey"},
                  {"code": "GHS", "currency-name":	"Ghanaian Cedi", "country": "Ghana"},
                  {"code": "GIP", "currency-name":	"Gibraltar Pound", "country": "Gibraltar"},
                  {"code": "GMD", "currency-name":	"Gambian Dalasi", "country": "Gambia"},
                  {"code": "GNF", "currency-name":	"Guinean Franc", "country": "Guinea"},
                  {"code": "GTQ", "currency-name":	"Guatemalan Quetzal", "country": "Guatemala"},
                  {"code": "GYD", "currency-name":	"Guyanese Dollar", "country": "Guyana"},
                  {"code": "HKD", "currency-name":	"Hong Kong Dollar", "country": "Hong Kong"},
                  {"code": "HNL", "currency-name":	"Honduran Lempira", "country": "Honduras"},
                  {"code": "HRK", "currency-name":	"Croatian Kuna", "country": "Croatia"},
                  {"code": "HTG", "currency-name":	"Haitian Gourde", "country": "Haiti"},
                  {"code": "HUF", "currency-name":	"Hungarian Forint", "country": "Hungary"},
                  {"code": "IDR", "currency-name":	"Indonesian Rupiah", "country": "Indonesia"},
                  {"code": "ILS", "currency-name":	"Israeli New Shekel", "country": "Israel"},
                  {"code": "IMP", "currency-name":	"Manx Pound", "country": "Isle of Man"},
                  {"code": "INR", "currency-name":	"Indian Rupee", "country": "India"},
                  {"code": "IQD", "currency-name":	"Iraqi Dinar", "country": "Iraq"},
                  {"code": "IRR", "currency-name":	"Iranian Rial", "country": "Iran"},
                  {"code": "ISK", "currency-name":	"Icelandic Króna", "country": "Iceland"},
                  {"code": "JEP", "currency-name":	"Jersey Pound", "country": "Jersey"},
                  {"code": "JMD", "currency-name":	"Jamaican Dollar", "country": "Jamaica"},
                  {"code": "JOD", "currency-name":	"Jordanian Dinar", "country": "Jordan"},
                  {"code": "JPY", "currency-name":	"Japanese Yen", "country": "Japan"},
                  {"code": "KES", "currency-name":	"Kenyan Shilling", "country": "Kenya"},
                  {"code": "KGS", "currency-name":	"Kyrgyzstani Som", "country": "Kyrgyzstan"},
                  {"code": "KHR", "currency-name":	"Cambodian Riel", "country": "Cambodia"},
                  {"code": "KID", "currency-name":	"Kiribati Dollar", "country": "Kiribati"},
                  {"code": "KMF", "currency-name":	"Comorian Franc", "country": "Comoros"},
                  {"code": "KRW", "currency-name":	"South Korean Won", "country": "South Korea"},
                  {"code": "KWD", "currency-name":	"Kuwaiti Dinar", "country": "Kuwait"},
                  {"code": "KYD", "currency-name":	"Cayman Islands Dollar", "country": "Cayman Islands"},
                  {"code": "KZT", "currency-name":	"Kazakhstani Tenge", "country": "Kazakhstan"},
                  {"code": "LAK", "currency-name":	"Lao Kip", "country": "Laos"},
                  {"code": "LBP", "currency-name":	"Lebanese Pound", "country": "Lebanon"},
                  {"code": "LKR", "currency-name":	"Sri Lanka Rupee", "country": "Sri Lanka"},
                  {"code": "LRD", "currency-name":	"Liberian Dollar", "country": "Liberia"},
                  {"code": "LSL", "currency-name":	"Lesotho Loti", "country": "Lesotho"},
                  {"code": "LYD", "currency-name":	"Libyan Dinar", "country": "Libya"},
                  {"code": "MAD", "currency-name":	"Moroccan Dirham", "country": "Morocco"},
                  {"code": "MDL", "currency-name":	"Moldovan Leu", "country": "Moldova"},
                  {"code": "MGA", "currency-name":	"Malagasy Ariary", "country": "Madagascar"},
                  {"code": "MKD", "currency-name":	"Macedonian Denar", "country": "North Macedonia"},
                  {"code": "MMK", "currency-name":	"Burmese Kyat", "country": "Myanmar"},
                  {"code": "MNT", "currency-name":	"Mongolian Tögrög", "country": "Mongolia"},
                  {"code": "MOP", "currency-name":	"Macanese Pataca", "country": "Macau"},
                  {"code": "MRU", "currency-name":	"Mauritanian Ouguiya", "country": "Mauritania"},
                  {"code": "MUR", "currency-name":	"Mauritian Rupee", "country": "Mauritius"},
                  {"code": "MVR", "currency-name":	"Maldivian Rufiyaa", "country": "Maldives"},
                  {"code": "MWK", "currency-name":	"Malawian Kwacha", "country": "Malawi"},
                  {"code": "MXN", "currency-name":	"Mexican Peso", "country": "Mexico"},
                  {"code": "MYR", "currency-name":	"Malaysian Ringgit", "country": "Malaysia"},
                  {"code": "MZN", "currency-name":	"Mozambican Metical", "country": "Mozambique"},
                  {"code": "NAD", "currency-name":	"Namibian Dollar", "country": "Namibia"},
                  {"code": "NGN", "currency-name":	"Nigerian Naira", "country": "Nigeria"},
                  {"code": "NIO", "currency-name":	"Nicaraguan Córdoba", "country": "Nicaragua"},
                  {"code": "NOK", "currency-name":	"Norwegian Krone", "country": "Norway"},
                  {"code": "NPR", "currency-name":	"Nepalese Rupee", "country": "Nepal"},
                  {"code": "NZD", "currency-name":	"New Zealand Dollar", "country": "New Zealand"},
                  {"code": "OMR", "currency-name":	"Omani Rial", "country": "Oman"},
                  {"code": "PAB", "currency-name": "Panamanian Balboa", "country": "Panama"},
                  {"code": "PEN", "currency-name":	"Peruvian Sol", "country": "Peru"},
                  {"code": "PGK", "currency-name":	"Papua New Guinean Kina", "country": "Papua New Guinea"},
                  {"code": "PHP", "currency-name":	"Philippine Peso", "country": "Philippines"},
                  {"code": "PKR", "currency-name":	"Pakistani Rupee", "country": "Pakistan"},
                  {"code": "PLN", "currency-name":	"Polish Złoty", "country": "Poland"},
                  {"code": "PYG", "currency-name":	"Paraguayan Guaraní", "country": "Paraguay"},
                  {"code": "QAR", "currency-name":	"Qatari Riyal", "country": "Qatar"},
                  {"code": "RON", "currency-name":	"Romanian Leu", "country": "Romania"},
                  {"code": "RSD", "currency-name":	"Serbian Dinar", "country": "Serbia"},
                  {"code": "RUB", "currency-name":	"Russian Ruble", "country": "Russia"},
                  {"code": "RWF", "currency-name":	"Rwandan Franc", "country": "Rwanda"},
                  {"code": "SAR", "currency-name":	"Saudi Riyal", "country": "Saudi Arabia"},
                  {"code": "SBD", "currency-name":	"Solomon Islands Dollar", "country": "Solomon Islands"},
                  {"code": "SCR", "currency-name":	"Seychellois Rupee", "country": "Seychelles"},
                  {"code": "SDG", "currency-name":	"Sudanese Pound", "country": "Sudan"},
                  {"code": "SEK", "currency-name":	"Swedish Krona", "country": "Sweden"},
                  {"code": "SGD", "currency-name":	"Singapore Dollar", "country": "Singapore"},
                  {"code": "SHP", "currency-name":	"Saint Helena Pound", "country": "Saint Helena"},
                  {"code": "SLE", "currency-name":	"Sierra Leonean Leone", "country": "Sierra Leone"},
                  {"code": "SOS", "currency-name":	"Somali Shilling", "country": "Somalia"},
                  {"code": "SRD", "currency-name":	"Surinamese Dollar", "country": "Suriname"},
                  {"code": "SSP", "currency-name":	"South Sudanese Pound", "country": "South Sudan"},
                  {"code": "STN", "currency-name":	"São Tomé and Príncipe Dobra", "country": "São Tomé and Príncipe"},
                  {"code": "SYP", "currency-name":	"Syrian Pound", "country": "Syria"},
                  {"code": "SZL", "currency-name":	"Eswatini Lilangeni", "country": "Eswatini"},
                  {"code": "THB", "currency-name":	"Thai Baht", "country": "Thailand"},
                  {"code": "TJS", "currency-name":	"Tajikistani Somoni", "country": "Tajikistan"},
                  {"code": "TMT", "currency-name":	"Turkmenistan Manat", "country": "Turkmenistan"},
                  {"code": "TND", "currency-name":	"Tunisian Dinar", "country": "Tunisia"},
                  {"code": "TOP", "currency-name":	"Tongan Paʻanga", "country": "Tonga"},
                  {"code": "TRY", "currency-name":	"Turkish Lira", "country": "Turkey"},
                  {"code": "TTD", "currency-name":	"Trinidad and Tobago Dollar", "country": "Trinidad and Tobago"},
                  {"code": "TVD", "currency-name":	"Tuvaluan Dollar", "country": "Tuvalu"},
                  {"code": "TWD", "currency-name":	"New Taiwan Dollar", "country": "Taiwan"},
                  {"code": "TZS", "currency-name":	"Tanzanian Shilling", "country": "Tanzania"},
                  {"code": "UAH", "currency-name":	"Ukrainian Hryvnia", "country": "Ukraine"},
                  {"code": "UGX", "currency-name":	"Ugandan Shilling", "country": "Uganda"},
                  {"code": "USD", "currency-name":	"United States Dollar", "country": "United States"},
                  {"code": "UYU", "currency-name":	"Uruguayan Peso", "country": "Uruguay"},
                  {"code": "UZS", "currency-name":	"Uzbekistani So'm", "country": "Uzbekistan"},
                  {"code": "VES", "currency-name":	"Venezuelan Bolívar Soberano", "country": "Venezuela"},
                  {"code": "VND", "currency-name":	"Vietnamese Đồng", "country": "Vietnam"},
                  {"code": "VUV", "currency-name":	"Vanuatu Vatu", "country": "Vanuatu"},
                  {"code": "WST", "currency-name":	"Samoan Tālā", "country": "Samoa"},
                  {"code": "XAF", "currency-name":	"Central African CFA Franc", "country": "CEMAC"},
                  {"code": "XCD", "currency-name":	"East Caribbean Dollar", "country": "Organisation of Eastern Caribbean States"},
                  {"code": "XDR", "currency-name":	"Special Drawing Rights", "country": "International Monetary Fund"},
                  {"code": "XOF", "currency-name":	"West African CFA franc", "country": "CFA"},
                  {"code": "XPF", "currency-name":	"CFP Franc", "country": "Collectivités d'Outre-Mer"},
                  {"code": "YER", "currency-name":	"Yemeni Rial", "country": "Yemen"},
                  {"code": "ZAR", "currency-name":	"South African Rand", "country": "South Africa"},
                  {"code": "ZMW", "currency-name":	"Zambian Kwacha", "country": "Zambia"},
                  {"code": "ZWL", "currency-name":	"Zimbabwean Dollar", "country": "Zimbabwe"}]


    iso_countries = []
    for place in iso_code:
        iso_countries.append(place["country"])


    use_ang = ["Sint Maarten", "Curacao", "St Maarten"]
    use_bam = ["Bosnia"]
    use_cdf = ["DRC", "Congo", "The Congo"]
    use_usd = ["USA", "America", "Ecuador", "El Salvador", "The British Virgin Islands", "BVI", "British Virgin Islands", "The Turks and Caicos", "Turks and Caicos", "Timor and Leste", "Timor", "Leste", "Bonaire"]
    use_xaf = ["Gabon", "Cameroon", "Central African Republic", "Republic of the Congo", "Equatorial Guinea", "Chad"]
    use_xcd = ["Anguilla", "Antigua and Barbuda", "Antigua", "Barbuda", "Dominica", "Grenada", "Montserrat", "Saint Kitts and Nevis", "Saint Kitts", "Saint Lucia", "Saint Vincent and the Grenadines", "Saint Vincent", "Grenadines"]
    use_xof = ["Benin", "Burkina Faso", "Guinea-Bissau", "Mali", "Niger", "Ivory Coast", "Senegal", "Togo"]
    use_xpf = ["French Polynesia", "New Caledonia", "Wallis and Futuna", "Wallis", "Futuna"]
    use_euro = ["Netherlands",
                "Andorra",
                "Belgium",
                "Spain",
                "Guadeloupe",
                "Ireland",
                "Italy",
                "Austria",
                "Greece",
                "Croatia",
                "Cyprus",
                "Latvia",
                "Lithuania",
                "Luxembourg",
                "Malta",
                "Martinique",
                "Mayotte",
                "Principality of Monaco",
                "Portugal",
                "France",
                "French Guiana",
                "Reunion",
                "Saint Pierre and Miquelon",
                "Germany",
                "San Marino",
                "Slovakia",
                "Slovenia",
                "Finland",
                "Vatican City",
                "Estonia",
                "French Southern and Antarctic Lands",
                "Montenegro",
                "Saint Barthelemy",
                "Kosovo",
                "Åland Islands",
                "Saint Martin",
                "Europe"]

    use_gbp = ["England",
               "Scotland",
               "Northern Ireland",
               "Wales",
               "South Georgia and the South Sandwich Islands",
               "British Antarctic Territory",
               "Tristan da Cunha",
               "GB",
               "UK",
               "Great Britain"]


    current_country = []

    def country_search(country):
        if placename in use_euro:
            current_country.append("European Union")
        elif placename in use_gbp:
            current_country.append("United Kingdom")
        elif placename in use_ang:
            current_country.append("Netherlands Antilles")
        elif placename in use_bam:
            current_country.append("Bosnia and Herzegovina")
        elif placename in use_cdf:
            current_country.append("Democratic Republic of the Congo")
        elif placename in use_usd:
            current_country.append("United States")
        elif placename in use_xaf:
            current_country.append("CEMAC")
        elif placename in use_xcd:
            current_country.append("Organisation of Eastern Caribbean States")
        elif placename in use_xof:
            current_country.append("CFA")
        elif placename in use_xpf:
            current_country.append("Collectivités d'Outre-Mer")
        elif placename in iso_countries:
            current_country.append(placename)
        else:
            print("Please check the spelling.")
        return current_country


    country_iso_name = country_search(current_country)

    #print(country_iso_name)

    country_for_code = "".join(country_iso_name)
    def currency_search_1(iso_code, country):
      for d in iso_code:
        if (d['country'] == country):
            return d["code"]

    iso_code_found = currency_search_1(iso_code, country_for_code)
    #print(iso_code_found)
    return iso_code_found

print(iso_code_finder("France"))