# author: wudashan
import requests
import MySQLdb

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
requests.packages.urllib3.disable_warnings()


def is_timeout(url):
    try:
        requests.get(url, timeout=3, verify=False)
        return False
    except requests.exceptions.RequestException, e:
        print e
        return True


def main():
    print "google address ping start!"
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='root',
        db='google_spider',
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM googleUrl")
    results = cur.fetchall()
    for row in results:
        if (not is_timeout(row[1])):
            cur.execute("UPDATE googleUrl SET updatetime = now(), isvalid = 1 WHERE url='" + row[1] + "'")
        else:
            cur.execute("UPDATE googleUrl SET updatetime = now(), isvalid = 0 WHERE url='" + row[1] + "'")
    cur.close()
    conn.commit()
    conn.close()
    print "google address ping end!"


if __name__ == '__main__':
    main()