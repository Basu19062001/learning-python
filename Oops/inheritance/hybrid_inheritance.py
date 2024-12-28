class Grand:
  pass
class MomGrand:
  pass

class MyDad(Grand):
  pass

class MyMom(MomGrand):
  pass

class Me(MyMom,MyDad):
  pass

class MySisters(MyMom, MyDad):
  pass

class MyNieceAndNephew(MySisters):
  pass

#    Grand           MomGrand
  #     │                 │
  #  MyDad             MyMom
  #     │                 │
  #     └──────┬──────────┘
  #       _____│________
  #       |            |
  #       Me        MySisters
  #                    │
  #              MyNieceAndNephew
