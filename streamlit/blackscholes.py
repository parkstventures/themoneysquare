# black and scholes
# app using streamlit
# june 2020
# subu sangameswar#-----------------------------------------------------------------------


# blackscholes.py
# Ref https://introcs.cs.princeton.edu/python/21function/blackscholes.py.html
#-----------------------------------------------------------------------

import streamlit as st
import sys
import math

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0: return 0.0
    if z >  8.0: return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + total * phi(z)

#-----------------------------------------------------------------------

# Return standard Gaussian cdf with mean mu and stddev sigma.
# Use Taylor approximation.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

#-----------------------------------------------------------------------

# Black-Scholes formula.

def callPrice(s, x, r, sigma, t):
    a = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / \
        (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)
    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)

#-----------------------------------------------------------------------

# Accept s, x, r, sigma, and t from the command line and write
# the Black-Scholes value.

s     = 23.75
x     = 15.0
r     = .01
sigma = .35
t     = .5

st.title('Black Scholes Calculator')
st.info("interactive app for Black Scholes")

s = st.sidebar.number_input("stock price", min_value=5.0,  step=1.0, value=23.75)

x = st.sidebar.number_input("strike price", min_value=5.0,  step=1.0, value=15.0)

r = st.sidebar.slider(
    'risk free interest rate %',
    .01, .05,.01
)

sigma = st.sidebar.slider(
    'volatality (historical)%',
    .30, .40, .35
)

t = st.sidebar.slider(
    'time until expiration (years)',
    .1, .9, .5
)

m = callPrice(s, x, r, sigma, t)
#print(m)

st.write(f"stock price at time 0:  $**{s:.2f}**")
st.write(f"stock strike price:  $**{x:.2f}**")

st.write(f"continuously compounded risk-free rate: {r:2f}")
#print "sigma\tvolatility of the stock price per year:", sigma
#print "T\ttime to maturity in trading years:", T

md_results =  f"The call price **{m:.2f}**."
st.markdown(md_results)
#-----------------------------------------------------------------------

