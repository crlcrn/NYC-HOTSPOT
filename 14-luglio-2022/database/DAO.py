from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_borgo():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct Borough as borgo
                from nyc_wifi_hotspot_locations nwhl 
                order by borgo asc      
        
                """

        cursor.execute(query)

        for row in cursor:
            results.append(row['borgo'])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_nodi(borgo):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct nwhl.NTACode 
                from nyc_wifi_hotspot_locations nwhl 
                where Borough = %s
                """

        cursor.execute(query, (borgo, ))

        for row in cursor:
            results.append(row['NTACode'])

        cursor.close()
        conn.close()
        return results


    @staticmethod
    def get_archi(borgo):
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT 
                    a.NTACode AS n1,
                    b.NTACode AS n2,
                    COUNT(DISTINCT c.SSID) AS peso
                FROM 
                    nyc_wifi_hotspot_locations a,
                    nyc_wifi_hotspot_locations b,
                    nyc_wifi_hotspot_locations c
                WHERE 
                    a.Borough = b.Borough
                    AND a.NTACode < b.NTACode
                    AND c.Borough = a.Borough
                    AND (c.NTACode = a.NTACode OR c.NTACode = b.NTACode)
                    AND a.Borough = %s
                GROUP BY 
                    a.NTACode, b.NTACode
                HAVING 
                    peso > 0
                """

        cursor.execute(query, (borgo, ))

        for row in cursor:
            results.append((row['n1'], row['n2'], row['peso']))

        cursor.close()
        conn.close()
        return results
