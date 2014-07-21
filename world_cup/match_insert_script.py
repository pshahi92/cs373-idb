from wc_app.models import *

# match_dict = {'Argentina-Belgium': [60, 'Argentina', 1, 'Belgium', 0, 'Argentina', 'Estadio Nacional', '2014-07-05'], 'Russia-Korea Republic': [16, 'Russia', 1, 'Korea Republic', 1, 'Draw', 'Arena Pantanal', '2014-06-17'], "Colombia-Ivory Coast": [21, 'Colombia', 2, "Ivory Coast", 1, 'Colombia', 'Estadio Nacional', '2014-06-19'], 'Brazil-Mexico': [17, 'Brazil', 0, 'Mexico', 0, 'Draw', 'Estadio Castelao', '2014-06-17'], 'Nigeria-Argentina': [43, 'Nigeria', 2, 'Argentina', 3, 'Argentina', 'Estadio Beira-Rio', '2014-06-25'], 'France-Germany': [58, 'France', 0, 'Germany', 1, 'Germany', 'Estadio do Maracana', '2014-07-04'], 'Colombia-Uruguay': [50, 'Colombia', 2, 'Uruguay', 0, 'Colombia', 'Estadio do Maracana', '2014-06-28'], 'Argentina-Iran': [27, 'Argentina', 1, 'Iran', 0, 'Argentina', 'Estadio Mineirao', '2014-06-21'], 'Korea Republic-Algeria': [32, 'Korea Republic', 2, 'Algeria', 4, 'Algeria', 'Estadio Beira-Rio', '2014-06-22'], 'Argentina-Bosnia and Herzegovina': [11, 'Argentina', 2, 'Bosnia and Herzegovina', 1, 'Argentina', 'Estadio do Maracana', '2014-06-15'], 'Costa Rica-Greece': [52, 'Costa Rica', 1, 'Greece', 1, 'Costa Rica', 'Arena Pernambuco', '2014-06-29'], 'Honduras-Switzerland': [41, 'Honduras', 0, 'Switzerland', 3, 'Switzerland', 'Arena Amazonia', '2014-06-25'], 'Netherlands-Chile': [36, 'Netherlands', 2, 'Chile', 0, 'Netherlands', 'Arena de Sao Paulo', '2014-06-23'], 'Uruguay-England': [23, 'Uruguay', 2, 'England', 1, 'Uruguay', 'Arena de Sao Paulo', '2014-06-19'], 'Iran-Nigeria': [12, 'Iran', 0, 'Nigeria', 0, 'Draw', 'Arena da Baixada', '2014-06-16'], 'Switzerland-Ecuador': [9, 'Switzerland', 2, 'Ecuador', 1, 'Switzerland', 'Estadio Nacional', '2014-06-15'], 'Costa Rica-England': [40, 'Costa Rica', 0, 'England', 0, 'Draw', 'Estadio Mineirao', '2014-06-24'], 'Brazil-Croatia': [1, 'Brazil', 3, 'Croatia', 1, 'Brazil', 'Arena de Sao Paulo', '2014-06-12'], 'Nigeria-Bosnia and Herzegovina': [28, 'Nigeria', 1, 'Bosnia and Herzegovina', 0, 'Nigeria', 'Arena Pantanal', '2014-06-21'], 'Cameroon-Brazil': [33, 'Cameroon', 1, 'Brazil', 4, 'Brazil', 'Estadio Nacional', '2014-06-23'], 'Belgium-Russia': [31, 'Belgium', 1, 'Russia', 0, 'Belgium', 'Estadio do Maracana', '2014-06-22'], 'Australia-Netherlands': [20, 'Australia', 2, 'Netherlands', 3, 'Netherlands', 'Estadio Beira-Rio', '2014-06-18'], 'Argentina-Switzerland': [55, 'Argentina', 1, 'Switzerland', 0, 'Argentina', 'Arena de Sao Paulo', '2014-07-01'], 'Belgium-USA': [56, 'Belgium', 2, 'USA', 1, 'Belgium', 'Arena Fonte Nova', '2014-07-01'], 'France-Nigeria': [53, 'France', 2, 'Nigeria', 0, 'France', 'Estadio Nacional', '2014-06-30'], 'Italy-Costa Rica': [24, 'Italy', 0, 'Costa Rica', 1, 'Costa Rica', 'Arena Pernambuco', '2014-06-20'], 'Brazil-Colombia': [57, 'Brazil', 2, 'Colombia', 1, 'Brazil', 'Estadio Castelao', '2014-07-04'], 'Cameroon-Croatia': [18, 'Cameroon', 0, 'Croatia', 4, 'Croatia', 'Arena Amazonia', '2014-06-18'], "Ivory Coast-Japan": [6, "Ivory Coast", 2, 'Japan', 1, 'Ivory Coast', 'Arena Pernambuco', '2014-06-14'], 'USA-Germany': [45, 'USA', 0, 'Germany', 1, 'Germany', 'Arena Pernambuco', '2014-06-26'], 'Ecuador-France': [42, 'Ecuador', 0, 'France', 0, 'Draw', 'Estadio do Maracana', '2014-06-25'], 'Germany-Portugal': [13, 'Germany', 4, 'Portugal', 0, 'Germany', 'Arena Fonte Nova', '2014-06-16'], 'Korea Republic-Belgium': [47, 'Korea Republic', 0, 'Belgium', 1, 'Belgium', 'Arena de Sao Paulo', '2014-06-26'], 'Italy-Uruguay': [39, 'Italy', 0, 'Uruguay', 1, 'Uruguay', 'Estadio das Dunas', '2014-06-24'], 'Japan-Greece': [22, 'Japan', 0, 'Greece', 0, 'Draw', 'Estadio das Dunas', '2014-06-19'], 'Portugal-Ghana': [46, 'Portugal', 2, 'Ghana', 1, 'Portugal', 'Estadio Nacional', '2014-06-26'], 'Mexico-Cameroon': [2, 'Mexico', 1, 'Cameroon', 0, 'Mexico', 'Estadio das Dunas', '2014-06-13'], 'Germany-Algeria': [54, 'Germany', 2, 'Algeria', 1, 'Germany', 'Estadio Beira-Rio', '2014-06-30'], 'Spain-Chile': [19, 'Spain', 0, 'Chile', 2, 'Chile', 'Estadio do Maracana', '2014-06-18'], 'Spain-Netherlands': [3, 'Spain', 1, 'Netherlands', 5, 'Netherlands', 'Arena Fonte Nova', '2014-06-13'], 'England-Italy': [8, 'England', 1, 'Italy', 2, 'Italy', 'Arena Amazonia', '2014-06-14'], 'Chile-Australia': [4, 'Chile', 3, 'Australia', 1, 'Chile', 'Arena Pantanal', '2014-06-13'], 'Japan-Colombia': [37, 'Japan', 1, 'Colombia', 4, 'Colombia', 'Arena Pantanal', '2014-06-24'], 'Croatia-Mexico': [34, 'Croatia', 1, 'Mexico', 3, 'Mexico', 'Arena Pernambuco', '2014-06-23'], 'Switzerland-France': [25, 'Switzerland', 2, 'France', 5, 'France', 'Arena Fonte Nova', '2014-06-20'], 'Netherlands-Mexico': [51, 'Netherlands', 2, 'Mexico', 1, 'Netherlands', 'Estadio Castelao', '2014-06-29'], 'USA-Portugal': [30, 'USA', 2, 'Portugal', 2, 'Draw', 'Arena Amazonia', '2014-06-22'], 'Colombia-Greece': [5, 'Colombia', 3, 'Greece', 0, 'Colombia', 'Estadio Mineirao', '2014-06-14'], 'Honduras-Ecuador': [26, 'Honduras', 1, 'Ecuador', 2, 'Ecuador', 'Arena da Baixada', '2014-06-20'], 'Algeria-Russia': [48, 'Algeria', 1, 'Russia', 1, 'Draw', 'Arena da Baixada', '2014-06-26'], 'France-Honduras': [10, 'France', 3, 'Honduras', 0, 'France', 'Estadio Beira-Rio', '2014-06-15'], 'Ghana-USA': [14, 'Ghana', 1, 'USA', 2, 'USA', 'Estadio das Dunas', '2014-06-16'], 'Bosnia and Herzegovina-Iran': [44, 'Bosnia and Herzegovina', 3, 'Iran', 1, 'Bosnia and Herzegovina', 'Arena Fonte Nova', '2014-06-25'], 'Australia-Spain': [35, 'Australia', 0, 'Spain', 3, 'Spain', 'Arena da Baixada', '2014-06-23'], 'Brazil-Chile': [49, 'Brazil', 1, 'Chile', 1, 'Brazil', 'Estadio Mineirao', '2014-06-28'], "Greece-Ivory Coast": [38, 'Greece', 2, "Ivory Coast", 1, 'Greece', 'Estadio Castelao', '2014-06-24'], 'Germany-Ghana': [29, 'Germany', 2, 'Ghana', 2, 'Draw', 'Estadio Castelao', '2014-06-21'], 'Belgium-Algeria': [15, 'Belgium', 2, 'Algeria', 1, 'Belgium', 'Estadio Mineirao', '2014-06-17'], 'Uruguay-Costa Rica': [7, 'Uruguay', 1, 'Costa Rica', 3, 'Costa Rica', 'Estadio Castelao', '2014-06-14']}
match_dict = { "Ivory Coast-Japan" : [ 6, "Ivory Coast", 2, "Japan", 1, "Ivory Coast", "Arena Pernambuco", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469" ] , "Cameroon-Croatia" : [ 18, "Cameroon", 0, "Croatia", 4, "Croatia", "Arena Amazonia", "2014-06-18", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cmr_cro.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1891625 " ] , "Costa Rica-Greece" : [ 52, "Costa Rica", 1, "Greece", 1, "Costa Rica", "Arena Pernambuco", "2014-06-29", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/crc_gre.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1922645 " ] , "Cameroon-Brazil" : [ 33, "Cameroon", 1, "Brazil", 4, "Brazil", "Estadio Nacional", "2014-06-23", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cmr_bra.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1905926 " ] , "Belgium-USA" : [ 56, "Belgium", 2, "USA", 1, "Belgium", "Arena Fonte Nova", "2014-07-01", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bel_usa.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1927655 " ] , "France-Honduras" : [ 10, "France", 3, "Honduras", 0, "France", "Estadio Beira-Rio", "2014-06-15", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/fra_hon.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1884329" ] , "Portugal-Ghana" : [ 46, "Portugal", 2, "Ghana", 1, "Portugal", "Estadio Nacional", "2014-06-26", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/por_gha.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1914375 " ] , "Chile-Australia" : [ 4, "Chile", 3, "Australia", 1, "Chile", "Arena Pantanal", "2014-06-13", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/chi_aus.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1879607" ] , "France-Nigeria" : [ 53, "France", 2, "Nigeria", 0, "France", "Estadio Nacional", "2014-06-30", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/fra_nga.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1923879 " ] , "Brazil-Mexico" : [ 17, "Brazil", 0, "Mexico", 0, "Draw", "Estadio Castelao", "2014-06-17", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_mex.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1890294 " ] , "Netherlands-Mexico" : [ 51, "Netherlands", 2, "Mexico", 1, "Netherlands", "Estadio Castelao", "2014-06-29", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ned_mex.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1921641 " ] , "Argentina-Iran" : [ 27, "Argentina", 1, "Iran", 0, "Argentina", "Estadio Mineirao", "2014-06-21", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/arg_irn.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1900059 " ] , "Brazil-Chile" : [ 49, "Brazil", 1, "Chile", 1, "Brazil", "Estadio Mineirao", "2014-06-28", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_chi.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1919927 " ] , "Germany-Algeria" : [ 54, "Germany", 2, "Algeria", 1, "Germany", "Estadio Beira-Rio", "2014-06-30", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ger_alg.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1924923 " ] , "Brazil-Germany" : [ 61, "Brazil", 1, "Germany", 7, "Germany", "Estadio Mineirao", "2014-07-08", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_ger.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1940217 " ] , "Colombia-Greece" : [ 5, "Colombia", 3, "Greece", 0, "Colombia", "Estadio Mineirao", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/col_gre.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1880788" ] , "Germany-Argentina" : [ 64, "Germany", 1, "Argentina", 0, "Germany", "Estadio do Maracana", "2014-07-13", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ger_arg.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1949165 " ] , "Switzerland-France" : [ 25, "Switzerland", 2, "France", 5, "France", "Arena Fonte Nova", "2014-06-20", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/sui_fra.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1897790 " ] , "Spain-Chile" : [ 19, "Spain", 0, "Chile", 2, "Chile", "Estadio do Maracana", "2014-06-18", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/esp_chi.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892188 " ] , "England-Italy" : [ 8, "England", 1, "Italy", 2, "Italy", "Arena Amazonia", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/eng_ita.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882674" ] , "Honduras-Ecuador" : [ 26, "Honduras", 1, "Ecuador", 2, "Ecuador", "Arena da Baixada", "2014-06-20", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/hon_ecu.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena da Baixada+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1898484 " ] , "Brazil-Croatia" : [ 1, "Brazil", 3, "Croatia", 1, "Brazil", "Arena de Sao Paulo", "2014-06-12", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_cro.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1876413" ] , "USA-Portugal" : [ 30, "USA", 2, "Portugal", 2, "Draw", "Arena Amazonia", "2014-06-22", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/usa_por.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1902782 " ] , "Mexico-Cameroon" : [ 2, "Mexico", 1, "Cameroon", 0, "Mexico", "Estadio das Dunas", "2014-06-13", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/mex_cmr.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1878138" ] , "Germany-Portugal" : [ 13, "Germany", 4, "Portugal", 0, "Germany", "Arena Fonte Nova", "2014-06-16", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ger_por.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886825" ] , "Iran-Nigeria" : [ 12, "Iran", 0, "Nigeria", 0, "Draw", "Arena da Baixada", "2014-06-16", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/irn_nga.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena da Baixada+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1886374" ] , "Switzerland-Ecuador" : [ 9, "Switzerland", 2, "Ecuador", 1, "Switzerland", "Estadio Nacional", "2014-06-15", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/sui_ecu.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1883821" ] , "Argentina-Belgium" : [ 60, "Argentina", 1, "Belgium", 0, "Argentina", "Estadio Nacional", "2014-07-05", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/arg_bel.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1934814 " ] , "Costa Rica-England" : [ 40, "Costa Rica", 0, "England", 0, "Draw", "Estadio Mineirao", "2014-06-24", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/crc_eng.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1910401 " ] , "Australia-Netherlands" : [ 20, "Australia", 2, "Netherlands", 3, "Netherlands", "Estadio Beira-Rio", "2014-06-18", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/aus_ned.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1892629 " ] , "Netherlands-Costa Rica" : [ 59, "Netherlands", 0, "Costa Rica", 0, "Netherlands", "Arena Fonte Nova", "2014-07-05", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ned_crc.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1934129 " ] , "Japan-Greece" : [ 22, "Japan", 0, "Greece", 0, "Draw", "Estadio das Dunas", "2014-06-19", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/jpn_gre.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1895306 " ] , "Netherlands-Argentina" : [ 62, "Netherlands", 0, "Argentina", 0, "Argentina", "Arena de Sao Paulo", "2014-07-09", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ned_arg.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1942555 " ] , "Korea Republic-Belgium" : [ 47, "Korea Republic", 0, "Belgium", 1, "Belgium", "Arena de Sao Paulo", "2014-06-26", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/kor_bel.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1915301 " ] , "Ghana-USA" : [ 14, "Ghana", 1, "USA", 2, "USA", "Estadio das Dunas", "2014-06-16", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/gha_usa.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1887620" ] , "Ecuador-France" : [ 42, "Ecuador", 0, "France", 0, "Draw", "Estadio do Maracana", "2014-06-25", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ecu_fra.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1912388 " ] , "Nigeria-Argentina" : [ 43, "Nigeria", 2, "Argentina", 3, "Argentina", "Estadio Beira-Rio", "2014-06-25", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/nga_arg.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1912988 " ] , "Greece-Ivory Coast" : [ 38, "Greece", 2, "Ivory Coast", 1, "Greece", "Estadio Castelao", "2014-06-24", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/gre_civ.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1909112 " ] , "Brazil-Netherlands" : [ 63, "Brazil", 0, "Netherlands", 3, "Netherlands", "Estadio Nacional", "2014-07-12", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_ned.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1947343 " ] , "Netherlands-Chile" : [ 36, "Netherlands", 2, "Chile", 0, "Netherlands", "Arena de Sao Paulo", "2014-06-23", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ned_chi.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1907253 " ] , "Russia-Korea Republic" : [ 16, "Russia", 1, "Korea Republic", 1, "Draw", "Arena Pantanal", "2014-06-17", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/rus_kor.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1889171 " ] , "Belgium-Algeria" : [ 15, "Belgium", 2, "Algeria", 1, "Belgium", "Estadio Mineirao", "2014-06-17", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bel_alg.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Mineirao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1888684" ] , "Croatia-Mexico" : [ 34, "Croatia", 1, "Mexico", 3, "Mexico", "Arena Pernambuco", "2014-06-23", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cro_mex.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1905847 " ] , "Argentina-Bosnia and Herzegovina" : [ 11, "Argentina", 2, "Bosnia and Herzegovina", 1, "Argentina", "Estadio do Maracana", "2014-06-15", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/arg_bih.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1885053" ] , "Brazil-Colombia" : [ 57, "Brazil", 2, "Colombia", 1, "Brazil", "Estadio Castelao", "2014-07-04", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bra_col.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1932297 " ] , "Uruguay-England" : [ 23, "Uruguay", 2, "England", 1, "Uruguay", "Arena de Sao Paulo", "2014-06-19", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/uru_eng.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1895979 " ] , "USA-Germany" : [ 45, "USA", 0, "Germany", 1, "Germany", "Arena Pernambuco", "2014-06-26", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/usa_ger.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1914374 " ] , "Germany-Ghana" : [ 29, "Germany", 2, "Ghana", 2, "Draw", "Estadio Castelao", "2014-06-21", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ger_gha.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1901499 " ] , "Colombia-Uruguay" : [ 50, "Colombia", 2, "Uruguay", 0, "Colombia", "Estadio do Maracana", "2014-06-28", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/col_uru.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1920394 " ] , "Algeria-Russia" : [ 48, "Algeria", 1, "Russia", 1, "Draw", "Arena da Baixada", "2014-06-26", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/alg_rus.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena da Baixada+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1915302 " ] , "Nigeria-Bosnia and Herzegovina" : [ 28, "Nigeria", 1, "Bosnia and Herzegovina", 0, "Nigeria", "Arena Pantanal", "2014-06-21", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/nga_bih.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1900738 " ] , "France-Germany" : [ 58, "France", 0, "Germany", 1, "Germany", "Estadio do Maracana", "2014-07-04", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/fra_ger.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1932880 " ] , "Bosnia and Herzegovina-Iran" : [ 44, "Bosnia and Herzegovina", 3, "Iran", 1, "Bosnia and Herzegovina", "Arena Fonte Nova", "2014-06-25", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bih_irn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1912961 " ] , "Colombia-Ivory Coast" : [ 21, "Colombia", 2, "Ivory Coast", 1, "Colombia", "Estadio Nacional", "2014-06-19", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/col_civ.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Nacional+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1894443 " ] , "Korea Republic-Algeria" : [ 32, "Korea Republic", 2, "Algeria", 4, "Algeria", "Estadio Beira-Rio", "2014-06-22", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/kor_alg.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Beira-Rio+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1904718 " ] , "Italy-Uruguay" : [ 39, "Italy", 0, "Uruguay", 1, "Uruguay", "Estadio das Dunas", "2014-06-24", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ita_uru.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio das Dunas+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1910373 " ] , "Japan-Colombia" : [ 37, "Japan", 1, "Colombia", 4, "Colombia", "Arena Pantanal", "2014-06-24", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/jpn_col.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pantanal+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1909142 " ] , "Uruguay-Costa Rica" : [ 7, "Uruguay", 1, "Costa Rica", 3, "Costa Rica", "Estadio Castelao", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/uru_crc.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio Castelao+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1882075" ] , "Belgium-Russia" : [ 31, "Belgium", 1, "Russia", 0, "Belgium", "Estadio do Maracana", "2014-06-22", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/bel_rus.jpg", "https://www.google.com/maps/embed/v1/place?q=Estadio do Maracana+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1903732 " ] , "Honduras-Switzerland" : [ 41, "Honduras", 0, "Switzerland", 3, "Switzerland", "Arena Amazonia", "2014-06-25", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/hon_sui.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1912442 " ] , "Italy-Costa Rica" : [ 24, "Italy", 0, "Costa Rica", 1, "Costa Rica", "Arena Pernambuco", "2014-06-20", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/ita_crc.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1897124 " ] , "Argentina-Switzerland" : [ 55, "Argentina", 1, "Switzerland", 0, "Argentina", "Arena de Sao Paulo", "2014-07-01", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/arg_sui.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena de Sao Paulo+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1926556 " ] , "Spain-Netherlands" : [ 3, "Spain", 1, "Netherlands", 5, "Netherlands", "Arena Fonte Nova", "2014-06-13", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/esp_ned.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Fonte Nova+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1878787" ] , "Australia-Spain" : [ 35, "Australia", 0, "Spain", 3, "Spain", "Arena da Baixada", "2014-06-23", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/aus_esp.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena da Baixada+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1907247 " ] } 

for key in match_dict:
	score_cat = str(match_dict[key][2]) + "-" + str(match_dict[key][4])
	Match.objects.create(match_num = match_dict[key][0], country_A = Country.objects.get(country_name = match_dict[key][1]), country_B = Country.objects.get(country_name = match_dict[key][3]), winner = match_dict[key][5], score = score_cat, location = match_dict[key][6], match_date = match_dict[key][7], merge_flag = match_dict[key][8], map_location = match_dict[key][9], highlight_url= match_dict[key][10]).save()
  # match_num = models.IntegerField(default=0)
  #   # country_AB = models.CharField(max_length=200)
  #   country_A = models.ForeignKey(Country, related_name='country_A')
  #   country_B = models.ForeignKey(Country, related_name='country_B')
  #   winner = models.CharField(max_length=200)
  #   score = models.CharField(max_length=64)
  #   location = models.CharField(max_length=200)
  #   match_date = models.DateField()
  #   merge_flag = models.CharField(max_length=500)
  #   versus_flag = models.CharField(max_length=500)
  #   map_location = models.CharField(max_length=500)
  #   highlight_url = models.CharField(max_length=500)



# Match.objects.create(match_num = match_dict['Argentina-Belgium'][0], country_A = Country.objects.get(country_name = match_dict['Argentina-Belgium'][1]), country_B = Country.objects.get(country_name = match_dict['Argentina-Belgium'][3]), winner = match_dict['Argentina-Belgium'][5], score = "score_cat", location = match_dict['Argentina-Belgium'][6], match_date = match_dict['Argentina-Belgium'][7]).save()