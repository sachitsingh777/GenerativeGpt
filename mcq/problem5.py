from flask import Flask, jsonify,request

app=Flask(__name__)

post={}
post_id=0
@app.route("/",methods=["GETS"])
def all_post():
    return jsonify(post)

@app.route("/create",method=["POST"])
def create_post():
    username=request.form.get("username")
    caption=request.form.get("caption")

    new_post={
        "id":post_id,
        "username":username,
        "caption":caption,
        "like":0,
        "comment":[]
    }
    post.append(new_post)
    post_id=post_id+1

    return jsonify(new_post)

@app.route("/delete/<int:post_id",method=["DELETE"])
def delete_post(post_id):
    if post[id]==post_id:
        post.remove(post)
        return jsonify({"msg":"delete post"})
    return jsonify({"err":"not found"})    

@app.route("/like/<int:post_id",method=["DELETE"])
def like_post(post_id):
    if post[id]==post_id:
        post["like"]+=1
        return jsonify({"msg":"like post"})
    return jsonify({"err":"not found"})  

@app.route("/like/<int:post_id",method=["DELETE"])
def like_post(post_id):
    if post[id]==post_id:
        post["like"]+=1
        return jsonify({"msg":"like post"})
    return jsonify({"err":"not found"})  


@app.route("/comment/<int:post_id",method=["DELETE"])
def comment_post(post_id):
    comment=request.form.get("comment")
    if post[id]==post_id:
        post["comment"].append(comment)
        return jsonify({"msg":"comment post"})
    return jsonify({"err":"not found"})  

if __name__==__main__:
app.run()