from django.shortcuts import render, redirect

# Create your views here.

from django.db import connection

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def create(request):
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                              maker 	CHAR(5),
                              model 	INT PRIMARY KEY,
                              type  	CHAR(50)
                          );
                          CREATE TABLE IF NOT EXISTS pcs(
                              model 	INT PRIMARY KEY,
                              speed 	FLOAT,
                              ram   	INT,
                              hd    	INT,
                              price 	INT
                          );
                          CREATE TABLE IF NOT EXISTS laptops(
                              model	    INT PRIMARY KEY,
                              speed	    FLOAT,
                              ram		INT,
                              hd		INT,
                              screen	FLOAT,
                              price	    INT
                          );
                          CREATE TABLE IF NOT EXISTS printers(
                              model	    INT PRIMARY KEY,
                              color 	CHAR(10),
                              type  	CHAR(10),
                              price	    INT
                          );
                          """)
    return render(request, 'myApp/create.html')


def insert(request):
    outputProducts = []
    outputPCs = []
    outputLaptops = []
    outputPrinters = []
    with connection.cursor() as cursor:
        cursor.execute("""INSERT IGNORE INTO products (maker, model, type)
                                  VALUES('A' , 1001, 'pc'),
                                  ('A' , 1002, 'pc'),
                                  ('A' , 1003, 'pc'),
                                  ('A' , 2004, 'laptop'),
                                  ('A' , 2005, 'laptop'),
                                  ('A' , 2006, 'laptop'),
                                  ('B' , 1004, 'pc'),
                                  ('B' , 1005, 'pc'),
                                  ('B' , 1006, 'pc'),
                                  ('B' , 2007, 'laptop'),
                                  ('C' , 1007, 'pc'),
                                  ('D' , 1008, 'pc'),
                                  ('D' , 1009, 'pc'),
                                  ('D' , 1010, 'pc'),
                                  ('D' , 3004, 'printer'),
                                  ('D' , 3005, 'printer'),
                                  ('E' , 1011, 'pc'),
                                  ('E' , 1012, 'pc'),
                                  ('E' , 1013, 'pc'),
                                  ('E' , 2001, 'laptop'),
                                  ('E' , 2002, 'laptop'),
                                  ('E' , 2003, 'laptop'),
                                  ('E' , 3001, 'printer'),
                                  ('E' , 3002, 'printer'),
                                  ('E' , 3003, 'printer'),
                                  ('F' , 2008, 'laptop'),
                                  ('F' , 2009, 'laptop'),
                                  ('G' , 2010, 'laptop'),
                                  ('H' , 3006, 'printer'),
                                  ('H' , 3007, 'printer');

                                  INSERT IGNORE INTO pcs (model, speed, ram, hd, price)
                                  VALUES (1001, 2.66, 1024, 250, 2114),
                                  (1002, 2.10, 512, 250, 995),
                                  (1003, 1.42, 512, 80, 478),
                                  (1004, 2.80, 1024, 250, 649),
                                  (1005, 3.20, 512, 250, 630),
                                  (1006, 3.20, 1024, 320, 1049),
                                  (1007, 2.20, 1024, 200, 510),
                                  (1008, 2.20, 2048, 250, 770),
                                  (1009, 2.00, 1024, 250, 650),
                                  (1010, 2.80, 2048, 300, 770),
                                  (1011, 1.86, 2048, 160, 959),
                                  (1012, 2.80, 1024, 160, 649),
                                  (1013, 3.06, 512, 80, 529);

                                  INSERT IGNORE INTO laptops (model, speed, ram, hd, screen, price)
                                  VALUES (2001, 2.00, 2048, 240, 20.1, 3673),
                                  (2002, 1.73, 1024, 80, 17.0, 949),
                                  (2003, 1.80, 512, 60, 15.4, 549),
                                  (2004, 2.00, 512, 60, 13.3, 1150),
                                  (2005, 2.16, 1024, 120, 17.0, 2500),
                                  (2006, 2.00, 2048, 80, 15.4, 1700),
                                  (2007, 1.83, 1024, 120, 17.0, 2500),
                                  (2008, 1.60, 1024, 100, 15.4, 900),
                                  (2009, 1.60, 512, 80, 14.1, 680),
                                  (2010, 2.00, 2048, 160, 15.4, 2300);

                                  INSERT IGNORE INTO printers (model, color, type, price)
                                  VALUES (3001, 'true', 'ink-jet', 99),
                                  (3002, 'false', 'laser', 239),
                                  (3003, 'true', 'laser', 899),
                                  (3004, 'true', 'ink-jet', 120),
                                  (3005, 'false', 'laser', 120),
                                  (3006, 'true', 'ink-jet', 100),
                                  (3007, 'true', 'laser', 200);
                                   """)
        sqlQueryProducts = "SELECT * FROM products;"
        cursor.execute(sqlQueryProducts)

        fetchResultProducts = cursor.fetchall()
        sqlQueryPCs = "SELECT * FROM pcs;"
        cursor.execute(sqlQueryPCs)
        fetchResultPCs = cursor.fetchall()

        sqlQueryLaptops = "SELECT * FROM laptops;"
        cursor.execute(sqlQueryLaptops)
        fetchResultLaptops = cursor.fetchall()

        sqlQueryPrinters = "SELECT * FROM printers;"
        cursor.execute(sqlQueryPrinters)
        fetchResultPrinters = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultProducts:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type':temp[2]}
            outputProducts.append(eachRow)

        for temp in fetchResultPCs:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
            outputPCs.append(eachRow)

        for temp in fetchResultLaptops:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3],
                       'screen': temp[4], 'price': temp[5]}
            outputLaptops.append(eachRow)

        for temp in fetchResultPrinters:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinters.append(eachRow)

    return render(request, 'myApp/insert.html', {"products": outputProducts,
                                                "pcs": outputPCs,
                                                "laptops": outputLaptops,
                                                "printers": outputPrinters,})


def q1(request):
    outputOfQuery1 = []

    with connection.cursor() as cursor:
        sqlQuery1 = "SELECT AVG(hd) FROM pcs;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery1:
            eachRow = {'avgHDSizePC': temp[0]}
            outputOfQuery1.append(eachRow)

    return render(request, 'myApp/q1.html', {"output1": outputOfQuery1[0]})


def q2(request):
    outputOfQuery2 = []

    with connection.cursor() as cursor:
        sqlQuery2 = """SELECT maker, AVG(speed)
                           FROM products NATURAL JOIN laptops
                           GROUP BY maker;
                        """
        cursor.execute(sqlQuery2)
        fetchResultQuery2 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery2:
            eachRow = {'maker': temp[0], 'avgSpeedLaptop': temp[1]}
            outputOfQuery2.append(eachRow)

    return render(request, 'myApp/q2.html', {"output2": outputOfQuery2})


def q3(request):
    outputOfQuery3 = []

    with connection.cursor() as cursor:
        sqlQuery3 = """SELECT model, price
                           FROM products NATURAL JOIN laptops
                           WHERE maker IN (
                                SELECT maker
                                FROM products NATURAL JOIN laptops
                                GROUP BY maker HAVING COUNT(model) = 1)
                                """
        cursor.execute(sqlQuery3)
        fetchResultQuery3 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery3:
            eachRow = {'model': temp[0], 'price': temp[1]}
            outputOfQuery3.append(eachRow)

    return render(request, 'myApp/q3.html', {"output3": outputOfQuery3})


def q4(request):
    outputOfQuery4 = []

    with connection.cursor() as cursor:
        sqlQuery4 = """SELECT printers.model, price
                           FROM products, printers
                           WHERE products.model = printers.model AND price IN (
                               SELECT MAX(price)
                               FROM products, printers
                               WHERE products.model = printers.model
                               GROUP BY maker)
                        """
        cursor.execute(sqlQuery4)
        fetchResultQuery4 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultQuery4:
            eachRow = {'model': temp[0], 'price': temp[1]}
            outputOfQuery4.append(eachRow)

    return render(request, 'myApp/q4.html', {"output4": outputOfQuery4})


def clear(request):
    with connection.cursor() as cursor:
        cursor.execute("""DROP TABLE products;
                          DROP TABLE pcs;
                          DROP TABLE laptops;
                          DROP TABLE printers;
                          """)
    return render(request, 'myApp/clear.html')


def display(request):
    outputProducts = []
    outputPCs = []
    outputLaptops = []
    outputPrinters = []
    outputOfQuery1 = []
    outputOfQuery2 = []
    outputOfQuery3 = []
    outputOfQuery4 = []
    # with connection.cursor() as cursor:
    #     sqlQueryProducts = "SELECT * FROM products;"
    #     cursor.execute(sqlQueryProducts)
    #
    #     fetchResultProducts = cursor.fetchall()
    #     sqlQueryPCs = "SELECT * FROM pcs;"
    #     cursor.execute(sqlQueryPCs)
    #     fetchResultPCs = cursor.fetchall()
    #
    #     sqlQueryLaptops = "SELECT * FROM laptops;"
    #     cursor.execute(sqlQueryLaptops)
    #     fetchResultLaptops = cursor.fetchall()
    #
    #     sqlQueryPrinters = "SELECT * FROM printers;"
    #     cursor.execute(sqlQueryPrinters)
    #     fetchResultPrinters = cursor.fetchall()
    #
    #     sqlQuery1 = "SELECT AVG(hd) FROM pcs;"
    #     cursor.execute(sqlQuery1)
    #     fetchResultQuery1 = cursor.fetchall()
    #
    #     sqlQuery2 = """SELECT maker, AVG(speed)
    #                    FROM products NATURAL JOIN laptops
    #                    GROUP BY maker;
    #                 """
    #     cursor.execute(sqlQuery2)
    #     fetchResultQuery2 = cursor.fetchall()
    #
    #     sqlQuery3 = """SELECT model, price
    #                    FROM products NATURAL JOIN laptops
    #                    WHERE maker IN (
    #                         SELECT maker
    #                         FROM products NATURAL JOIN laptops
    #                         GROUP BY maker HAVING COUNT(model) = 1)
    #                         """
    #     cursor.execute(sqlQuery3)
    #     fetchResultQuery3 = cursor.fetchall()
    #
    #     sqlQuery4 = """SELECT printers.model, price
    #                    FROM products, printers
    #                    WHERE products.model = printers.model AND price IN (
    #                        SELECT MAX(price)
    #                        FROM products, printers
    #                        WHERE products.model = printers.model
    #                        GROUP BY maker)
    #                 """
    #     cursor.execute(sqlQuery4)
    #     fetchResultQuery4 = cursor.fetchall()
    #
    #     connection.commit()
    #     connection.close()
    #
    #     for temp in fetchResultProducts:
    #         eachRow = {'maker': temp[0], 'model': temp[1], 'type':temp[2]}
    #         outputProducts.append(eachRow)
    #
    #     for temp in fetchResultPCs:
    #         eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'price': temp[4]}
    #         outputPCs.append(eachRow)
    #
    #     for temp in fetchResultLaptops:
    #         eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3],
    #                    'screen': temp[4], 'price': temp[5]}
    #         outputLaptops.append(eachRow)
    #
    #     for temp in fetchResultPrinters:
    #         eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
    #         outputPrinters.append(eachRow)
    #
    #     for temp in fetchResultQuery1:
    #         eachRow = {'avgHDSizePC': temp[0]}
    #         outputOfQuery1.append(eachRow)
    #
    #     for temp in fetchResultQuery2:
    #         eachRow = {'maker': temp[0],'avgSpeedLaptop': temp[1]}
    #         outputOfQuery2.append(eachRow)
    #
    #     for temp in fetchResultQuery3:
    #         eachRow = {'model': temp[0], 'price': temp[1]}
    #         outputOfQuery3.append(eachRow)
    #
    #     for temp in fetchResultQuery4:
    #         eachRow = {'model': temp[0], 'price': temp[1]}
    #         outputOfQuery4.append(eachRow)


    return render(request, 'myApp/index.html', {"products": outputProducts,
                                                "pcs": outputPCs,
                                                "laptops": outputLaptops,
                                                "printers": outputPrinters,
                                                "output1": outputOfQuery1,
                                                "output2": outputOfQuery2,
                                                "output3": outputOfQuery3,
                                                "output4": outputOfQuery4})
