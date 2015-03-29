from matching import Category, Item, db

db.create_all()
db.session.add(Category("Beer"))
db.session.add(Category("Food"))
db.session.add(Category("Wine"))
#db.session.add(Item("Corona", "Mexico", ca, "im.jpg"))
db.session.commit()

categories = Category.query.all()
print categories



#beer = Category.query.filter_by(name = "Beers").first()
#print beer
#print len(items)

#for c in categories:
#	print c.id

# print cat1.items.all()

# print cat1.name, "NAME"
# print cat1.items.all()

# print Category.query.all()
# beer = Item.query.filter_by(title = "Corona").first()
# print beer.title, beer.id