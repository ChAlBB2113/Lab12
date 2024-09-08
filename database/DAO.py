from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def ottieniNodi(nazione):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct (Retailer_code) as r
                    from go_retailers
                    where Country=%s
                                     """
        cursor.execute(query, (nazione,))
        for row in cursor:
            result.append(row["r"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottieniNazioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct (Country) as n
                            from go_retailers
                            
                                             """
        cursor.execute(query, ())
        for row in cursor:
            result.append(row["n"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottieniArchi(nazione, anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select t.r1 as rr1, t.r2 as rr2, count(*) as peso
from
			(select g1.Retailer_code as r1 , g2.Retailer_code as r2, g1.Product_number as p
			from go_daily_sales g1, go_daily_sales g2
			where year(g1.`Date`)=%s and year(g2.`Date`)=%s
			and g1.Retailer_code in (select distinct (Retailer_code) as r
			                    from go_retailers
			                    where Country=%s)
			and g2.Retailer_code in (select distinct (Retailer_code) as r
			                    from go_retailers
			                    where Country=%s)
			and g1.Product_number=g2.Product_number
			and g1.Retailer_code<g2.Retailer_code 
			group by r2, r1, p) as t 
group by rr1, rr2
                                         """
        #prima un group by anche sui prodotti perchè si vuole
        #quanti prodotti diversi ogni diversa coppia di retailers  ha venduto in comune,
        #poi altro group by sulla coppia di retailers per contare quanti sono quei diversi prodotti che ha venduto  in comune
        cursor.execute(query, (anno, anno, nazione, nazione))
        for row in cursor:
            result.append((row["rr1"], row["rr2"], row["peso"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def ottineiDizRetailersCodeName():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """select Retailer_code as c, Retailer_name as n
        from go_retailers
                                                     """
        cursor.execute(query, ())
        for row in cursor:
            result[row["c"]]=row["n"]

        cursor.close()
        conn.close()
        return result




