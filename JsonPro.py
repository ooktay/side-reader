#main test ve tests classlarim in icinde jsondaki butun tanimli elemanlar var. Main_test.parse_from_json(json_object)

#methodu icine bi json aldiginda json objesindeki gerekli elemanlari okuyup bu elemanlari kullanarak

#bir main_test objesi yaratir.

#Test classim da bu json dosyasindaki tests kismindaki elemanlar icin yarattim onun da kendine ozel parse json methodu var

#ve yine ayni islemi yapiyor.

#Main_Test.parse_from_json(json_object):

#input: json objesi (filepath ile alinabilir vs.)


#parsed_json maintest tipindeki obje icinde bir tane test listesi var, bu test listesinin icinde de testler var o testlerin id name ve commands i var
#bu commandslerde ayri bir liste her bir test icin o yuzden commandsden bi eleman cagirmak parsed_json.test[0].commands[] istedigimiz indexdeki elemani cagirabiliyoruz.
import json
#Reading a file
# f = open('jhipster.side', 'r+')
# # read()
# text = f.read()
# print(text)
# f.close()

class Main_Test:

    def __init__(self, id, version, url, tests, suites, urls, plugins):

        self.id = id
        self.version = version
        self.url = url
        self.tests = tests
        self.suites = suites
        self.urls = urls
        self.plugins = plugins

    def parse_from_json(json_object):

        if json_object is None:
            return None

        json_tests_list = json_object['tests']
        object_tests_list = []
        for json_test in json_tests_list:

            object_tests_list.append(Test.parse_from_json(json_test))

            return Main_Test(json_object["id"],
            json_object["version"],
            json_object["url"],
            object_tests_list,
            json_object["suites"],
            json_object["urls"],
            json_object["plugins"])

class Test:

    def __init__(self, id, name, commands):

        self.id = id
        self.name = name
        self.commands = commands

    def parse_from_json(json_object):

        if json_object is None:
            return None

        json_commands_list = json_object['commands']
        object_commands_list = []
        for json_test in json_commands_list:
            object_commands_list.append(Commands.parse_from_json(json_test))

        return Test(json_object["id"],
                    json_object["name"],
                    object_commands_list)


class Commands:

    def __init__(self, id, comment, command, target, targets, value):
        self.id = id
        self.comment = comment
        self.command = command
        self.target = target
        self.targets = targets
        self.value = value

    def parse_from_json(json_object):

        if json_object is None:
            return None

        return Commands(json_object["id"],
        json_object["comment"],
        json_object["command"],
        json_object["target"],
        json_object["targets"],
        json_object["value"])



with open("jhipster.side", "r") as read_file:

    data = json.load(read_file)
    parsed_json = Main_Test.parse_from_json(data)


    print(parsed_json.tests[0].commands[0].id)
    print(parsed_json.tests[0].id)
    print(parsed_json.tests[0].name)
    print(parsed_json.url)



