from flask import render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from . import user
from .. models import User, Role, db, Post
from forms import EditProfileForm, EditProfileAdminForm
from .. decorators import admin_required


@user.route('/info')
@login_required
def info():
    #import pdb; pdb.set_trace()
    return render_template('user/info.html')

@user.route('/sec')
@login_required
def secret():
    #import pdb; pdb.set_trace()
    return render_template('user/sec/secret.html')

@user.route('/<username>')
def user_home(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestamp.desc()).all()
    return render_template('user/user.html', user=user, posts=posts)

@user.route('/edit-profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        #current_user.sex = form.sex.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user_home', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('user/edit_profile.html', form=form)

@user.route('/edit-profile/<int:id>', methods=['GET','POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.sex = form.sex.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        #import pdb; pdb.set_trace()
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user_home', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.sex.data = user.sex
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('user/edit_profile.html', form=form, user=user)






