import numpy as np
import ipinfo
import argparse

#Euclidean distance function
def distance(co1, co2):
    return np.sqrt(pow(abs(co1[0] - co2[0]), 2) + pow(abs(co1[1] - co2[1]), 2))


class FruadFriction():
    def __init__(self, db_filePath, actoken):
        self.dbfilepath = db_filePath
        self.access_token = actoken
        self.data_dict = {}
        self.parse_previousData()

    #Read the IP file and create a dictionary of unique IPs,it's fraudulant status and it's location coordinates  
    def parse_previousData(self):
        with open(self.dbfilepath) as infile:
            for line in infile:
                _tmp = line.split()
                if _tmp[1] not in self.data_dict.keys():
                    _t = np.asarray(self.getloc(_tmp[1]).split(',')).astype(float)
                    #Converting latitudes from -90-+90 to 0-180 scale 
                    _t[0] = _t[0] + 90
                    #Converting longitudes from -180-+180 to 0-360 scale 
                    _t[1] = _t[1] + 180
                    self.data_dict[_tmp[1]] = {'fruad_type': _tmp[0],
                                               'loc': tuple(_t)}

    #Function to get location for each IP 
    def getloc(self, ip):
        handler = ipinfo.getHandler(self.access_token)
        details = handler.getDetails(ip)
        return details.loc

    #Function to retrieve Fraud Score by calculating Euclidean distance between queried IP and list of dictionary IPS
    def getfraudscore(self, query):
        queryLatLong = tuple(np.asarray(self.getloc(query).split(',')).astype(float))
        result = self.find_closestLatLong([self.data_dict[i]['loc'] for i in self.data_dict.keys()], queryLatLong)
        if self.data_dict[list(self.data_dict.keys())[result[0]]]['fruad_type'] is 'FRAUD':
            return result[1] * 2
        else:
            return result[1]

    #Retrieve minimum distance and it's location
    def find_closestLatLong(self, listCoordinates, query):
        _x = [tuple((idx, distance(tup, query))) for idx, tup in enumerate(listCoordinates)]
        return min(_x, key=lambda t: t[0])


def main(args):
    fruad = FruadFriction(args['filepath'], args['acessToken'])
    print('Score the query is {}'.format(fruad.getfraudscore('22.4.62.188')))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Fraud detection challenge from UnifyID. Please pass the fruad file db path and the access token.')
    parser.add_argument('-f', '--filepath', help='Filepath of the fruad db.', required=True)
    parser.add_argument('-t', '--acessToken', help='access token for ipinfo.io', required=True)
    args = vars(parser.parse_args())
    main(args)
