from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Cart, Product, Category, ProductOrder
from .forms import CheckoutForm, GetInTouchForm, UserReg, UserLog


class MainPage(ListView):
    context_object_name = 'products'
    template_name = 'product_shop/index.html'
    paginate_by = 4 # Change if you want to have more or less products on one page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.all().order_by('created_at')

class ShowCategories(ListView):
    template_name = 'product_shop/category.html'
    context_object_name = 'products'
    paginate_by = 2
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug']).order_by('created_at')


def contact_us(request):
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet mauris commodo quis imperdiet massa tincidunt. Fermentum leo vel orci porta. Amet est placerat in egestas erat imperdiet sed euismod nisi. Nibh ipsum consequat nisl vel pretium lectus quam id. Tortor vitae purus faucibus ornare suspendisse sed nisi. Mi ipsum faucibus vitae aliquet nec. Risus nullam eget felis eget nunc lobortis mattis aliquam. A diam sollicitudin tempor id eu nisl. Ornare arcu odio ut sem nulla pharetra diam sit amet. Eget nunc scelerisque viverra mauris in aliquam sem fringilla. Diam maecenas ultricies mi eget mauris pharetra et ultrices. Accumsan sit amet nulla facilisi. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae.Duis at tellus at urna condimentum mattis. Scelerisque felis imperdiet proin fermentum leo vel orci porta. Turpis egestas pretium aenean pharetra magna ac placerat. Mattis aliquam faucibus purus in massa tempor. Sapien nec sagittis aliquam malesuada bibendum. In cursus turpis massa tincidunt dui. Semper feugiat nibh sed pulvinar proin. Erat nam at lectus urna duis convallis. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Nisl pretium fusce id velit ut tortor pretium. Convallis a cras semper auctor neque vitae. Fringilla ut morbi tincidunt augue. Metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices.Egestas quis ipsum suspendisse ultrices gravida. Tortor dignissim convallis aenean et tortor at risus. Netus et malesuada fames ac turpis egestas integer. Malesuada fames ac turpis egestas sed. Magna fermentum iaculis eu non diam. Neque gravida in fermentum et sollicitudin ac orci. Elementum facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Dolor sit amet consectetur adipiscing elit duis. Interdum varius sit amet mattis vulputate enim nulla aliquet porttitor. Ut faucibus pulvinar elementum integer. Duis convallis convallis tellus id. Habitasse platea dictumst vestibulum rhoncus est pellentesque. Ornare arcu dui vivamus arcu felis bibendum ut tristique et. Commodo sed egestas egestas fringilla phasellus. Nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Sodales ut eu sem integer vitae justo eget magna fermentum. At urna condimentum mattis pellentesque id nibh tortor id aliquet. Nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut.Eu volutpat odio facilisis mauris sit amet. Dolor sit amet consectetur adipiscing elit. Feugiat in ante metus dictum. In dictum non consectetur a erat nam. Lorem sed risus ultricies tristique nulla aliquet. Vitae tempus quam pellentesque nec nam. Eu nisl nunc mi ipsum faucibus vitae aliquet nec. Sed velit dignissim sodales ut. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Non tellus orci ac auctor augue mauris. Facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Nunc id cursus metus aliquam eleifend. Massa eget egestas purus viverra. Feugiat in fermentum posuere urna nec. Viverra mauris in aliquam sem fringilla.Aliquet eget sit amet tellus. Sagittis eu volutpat odio facilisis mauris sit. Nisl nunc mi ipsum faucibus. Rutrum tellus pellentesque eu tincidunt tortor aliquam. Senectus et netus et malesuada fames ac turpis egestas. Congue nisi vitae suscipit tellus mauris a diam maecenas sed. Non blandit massa enim nec dui nunc mattis enim ut. Quam nulla porttitor massa id neque aliquam. Egestas erat imperdiet sed euismod nisi porta. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed. Risus sed vulputate odio ut enim. Fringilla est ullamcorper eget nulla facilisi. Tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque.'
            mail = send_mail(form.cleaned_data['subject'], lorem, settings.EMAIL_HOST_USER, [form.cleaned_data['email']], fail_silently=True)
            if mail:
               form.save()
               messages.success(request, 'All Successed')
               return redirect('/')
            else:
                messages.error(request, 'Error')
    else:
        form = GetInTouchForm()
    return render(request, 'product_shop/contact_us.html', {'form':form})

class Search(ListView):
    context_object_name = 'products'
    template_name = 'product_shop/search.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('s')).order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        context['s1'] = f" `{self.request.GET.get('s')}`"
        context['categories'] = Category.objects.all()
        return context


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product_shop/product_detail.html', {'product':product})


@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart, created = Cart.objects.get_or_create(user=request.user, active=True)
    order, created = ProductOrder.objects.get_or_create(product=product, cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, 'Cart Updated')
    return redirect('/')

@login_required
def product_in_cart(request):
    cart = Cart.objects.filter(user=request.user)
    product = ProductOrder.objects.filter(cart__in=cart)
    return render(request, 'product_shop/test.html', {'products':product})

@login_required
def remove_from_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart = Cart.objects.get(user=request.user, active=True)
    cart.remove_from_cart(product_slug)
    messages.success(request, 'Cart Updated')
    return redirect('/')

def registration(request):
   if request.method == 'POST':
       form = UserReg(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           messages.success(request, 'Success') 
           return redirect('/')
       else:
           print(form.errors)
           messages.error(request, 'Error') 
   else:
      form = UserReg()
   return render(request, 'product_shop/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLog(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'All Success')
            return redirect('/')
        else:
            print(form.errors)
            messages.error(request, 'Something Went Wrong. Try Again')
    else:
        form = UserLog()
    return render(request, 'product_shop/login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Success')
    return redirect('/')


class Checkout(LoginRequiredMixin, CreateView):
    form_class = CheckoutForm
    template_name = 'product_shop/checkout.html'
    success_url = '/'
    context_object_name = 'form'
    raise_exception = True

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.cleaned_data['products'] = ProductOrder.objects.filter(cart__user=self.request.user)

        lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sit amet mauris commodo quis imperdiet massa tincidunt. Fermentum leo vel orci porta. Amet est placerat in egestas erat imperdiet sed euismod nisi. Nibh ipsum consequat nisl vel pretium lectus quam id. Tortor vitae purus faucibus ornare suspendisse sed nisi. Mi ipsum faucibus vitae aliquet nec. Risus nullam eget felis eget nunc lobortis mattis aliquam. A diam sollicitudin tempor id eu nisl. Ornare arcu odio ut sem nulla pharetra diam sit amet. Eget nunc scelerisque viverra mauris in aliquam sem fringilla. Diam maecenas ultricies mi eget mauris pharetra et ultrices. Accumsan sit amet nulla facilisi. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae.Duis at tellus at urna condimentum mattis. Scelerisque felis imperdiet proin fermentum leo vel orci porta. Turpis egestas pretium aenean pharetra magna ac placerat. Mattis aliquam faucibus purus in massa tempor. Sapien nec sagittis aliquam malesuada bibendum. In cursus turpis massa tincidunt dui. Semper feugiat nibh sed pulvinar proin. Erat nam at lectus urna duis convallis. Egestas egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Nisl pretium fusce id velit ut tortor pretium. Convallis a cras semper auctor neque vitae. Fringilla ut morbi tincidunt augue. Metus aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices.Egestas quis ipsum suspendisse ultrices gravida. Tortor dignissim convallis aenean et tortor at risus. Netus et malesuada fames ac turpis egestas integer. Malesuada fames ac turpis egestas sed. Magna fermentum iaculis eu non diam. Neque gravida in fermentum et sollicitudin ac orci. Elementum facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Et egestas quis ipsum suspendisse ultrices gravida dictum fusce ut. Dolor sit amet consectetur adipiscing elit duis. Interdum varius sit amet mattis vulputate enim nulla aliquet porttitor. Ut faucibus pulvinar elementum integer. Duis convallis convallis tellus id. Habitasse platea dictumst vestibulum rhoncus est pellentesque. Ornare arcu dui vivamus arcu felis bibendum ut tristique et. Commodo sed egestas egestas fringilla phasellus. Nunc scelerisque viverra mauris in aliquam sem fringilla ut morbi. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Sodales ut eu sem integer vitae justo eget magna fermentum. At urna condimentum mattis pellentesque id nibh tortor id aliquet. Nulla aliquet porttitor lacus luctus accumsan tortor posuere ac ut.Eu volutpat odio facilisis mauris sit amet. Dolor sit amet consectetur adipiscing elit. Feugiat in ante metus dictum. In dictum non consectetur a erat nam. Lorem sed risus ultricies tristique nulla aliquet. Vitae tempus quam pellentesque nec nam. Eu nisl nunc mi ipsum faucibus vitae aliquet nec. Sed velit dignissim sodales ut. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis aliquam. Non tellus orci ac auctor augue mauris. Facilisis leo vel fringilla est ullamcorper eget nulla facilisi. Nunc id cursus metus aliquam eleifend. Massa eget egestas purus viverra. Feugiat in fermentum posuere urna nec. Viverra mauris in aliquam sem fringilla.Aliquet eget sit amet tellus. Sagittis eu volutpat odio facilisis mauris sit. Nisl nunc mi ipsum faucibus. Rutrum tellus pellentesque eu tincidunt tortor aliquam. Senectus et netus et malesuada fames ac turpis egestas. Congue nisi vitae suscipit tellus mauris a diam maecenas sed. Non blandit massa enim nec dui nunc mattis enim ut. Quam nulla porttitor massa id neque aliquam. Egestas erat imperdiet sed euismod nisi porta. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed. Risus sed vulputate odio ut enim. Fringilla est ullamcorper eget nulla facilisi. Tellus in hac habitasse platea dictumst vestibulum rhoncus est pellentesque.'
        send_mail('Your Order `Freshshop`', lorem, settings.EMAIL_HOST_USER, [form.cleaned_data['email']], fail_silently=True)
        
        form.save()
        messages.success(self.request, 'All Fine')
        return super(Checkout, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Something Went Wrong')
        return super(Checkout, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user)
        context['product'] = ProductOrder.objects.filter(cart__in=cart)
        product_total = ProductOrder.objects.filter(cart__in=cart).aggregate(Sum('total'))
        context['total'] = product_total['total__sum']
        return context