from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . models import Board, Newboard
from members.models import Member
# Create your views here.

@login_required
def board(request):
	boards = Board.objects.all()
	context = {'boards':boards}
	template = 'boards/board.html'
	return render(request, template, context)


def edit(request):
	boards = Board.objects.all()
	members = Member.objects.all()
	context = {'boards':boards, 'members': members}
	template = 'boards/details.html'
	return render(request, template, context)


def remove(request, id):
	try:
		the_id = request.session['board_id']
		board = Board.objects.get(id=the_id)
	except:
		return HttpResponseRedirect(reverse("cart"))

	newboard = Newboard.objects.get(id=id)
	newboard.delete()
	newboard.save()

	return HttpResponseRedirect(reverse("board")) 

def add(request, id):
	try:
		the_id = request.session['board_id']
	except:
		new_board = Board()
		new_board.save()
		request.session['board_id']= new_board.id 
		the_id = new_board.id

	board = Board.objects.get(id=the_id)

