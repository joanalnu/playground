c = 299792.458 # speed of light

# a structure used to define the parameters container
struct LCDM
    H0::Float64
    Ωm::Float64
    Ωλ::Float64
end

using QuadGK

# 1. hubble parameter evolution
function E(cosmo::LCDM, z)
    return sqrt(cosmo.Ωm * (1 + z)^3 + cosmo.Ωλ)
end

# 2. comoving distance
function comoving_distance(cosmo::LCDM, z)
    integral, _ = quadgk(x -> 1.0 / E(cosmo, x), 0, z)
    return (299792.458 / cosmo.H0) * integral
end

# 3. luminosity distance
function luminosity_distance(cosmo::LCDM, z)
    return (1 + z) * comoving_distance(cosmo, z)
end

# 4. hubble parameter
function H(cosmo::LCDM, z)
    return E(cosmo, z) / cosmo.H0
end

cosmo = LCDM(67.4, 0.315, 0.685)
z_array = range(0.0, 2.0, length=50)

# Broadcast the functions over the array using the '.'
d_L = luminosity_distance.(Ref(cosmo), z_array)
d_C = comoving_distance.(Ref(cosmo), z_array)
e = E.(Ref(cosmo), z_array)
h = H.(Ref(cosmo), z_array)

using UnicodePlots
plt = lineplot(z_array, d_L, title="Luminosity Distance vs Redshift", xlabel="z", ylabel="d_L (Mpc)")
display(plt)
plt = lineplot(z_array, d_C, title="Comoving Distance vs Redshift", xlabel="z", ylabel="d_C (Mpc)")
display(plt)

mplt = lineplot(z_array, d_L, title="Distance comparison", 
                xlabel="z",
                ylabel="distancevalues",
                name="d_L(z)")

lineplot!(mplt, z_array, d_C, name="d_C(z)")
display(mplt)






# -------------------------------------------

struct wCDM
    H0::Float64
    Ωm::Float64
    Ωλ::Float64
    w0::Float64 # Dark energy equation of state parameter
end

# Julia will automatically know which function to call based on the struct type!
function E(cosmo::wCDM, z)
    return sqrt(cosmo.Ωm * (1 + z)^3 + cosmo.Ωλ * (1 + z)^(3 * (1 + cosmo.w0)))
end
