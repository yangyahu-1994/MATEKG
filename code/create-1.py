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
            # print(dic['名称'])
            new_data = dic['名称']
            new_node = Node('military','名称',new_data,
                                  name=new_data
                                  )
            graph.create(new_node)
            # node_relationship(new_node, '属于', graph.nodes.match('二级', name='explosive').first())
            print('#############' + str(new_data) + "##########节点创建成功")
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