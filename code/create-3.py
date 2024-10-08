from py2neo import Graph, Node, Relationship
import json
import os
import io


graph = Graph('http://localhost:7474/browser/', username='neo4j', password='123')



def create_new_node(path):
    try:
        user = open(path, 'r', encoding="utf-8")
        for line in user.readlines():
            dic = json.loads(line)
            print(line)
            new_data = dic['图片']
            if new_data != '':
                if graph.nodes.match('图片', name=new_data).first() is None:
                    new_node = Node('military','图片',new_data,
                                          name = new_data
                                          )
                    graph.create(new_node)
                    node_relationship(
                        graph.nodes.match('名称', name = dic['名称']).first(),
                        '图片',
                        new_node
                    )
                    print('############# ' + str(new_data) + " ##########节点创建成功")
                else:
                    node_relationship(
                        graph.nodes.match('名称', name = dic['名称']).first(),
                        '图片',
                        graph.nodes.match('图片', name = new_data).first()
                    )
                    print('============= ' + str(new_data) + " =============节点创建成功")
            else:
                print('----------------------------------')
    except Exception as e:
        print(e)
        print('***' + str(new_data) + '***' + "节点关系创建失败")
        pass
        return




def read_json(path):
    user = open(path, encoding="utf-8").read()
    userDict = json.loads(user)
    return userDict




def node_relationship(source_node, rela, target_node):
    node_rel_relationship = Relationship(source_node, rela, target_node)
    node_rel_relationship['relation'] = rela
    graph.create(node_rel_relationship)




if __name__ == '__main__':
    fact_path = 'C:/Users/yyh1994/Desktop/military.json'
    create_new_node(fact_path)