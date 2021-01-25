# use jupyter data science notebook as parent image
# for more info and other jupyter stacks, see
# https://github.com/jupyter/docker-stacks
# as per jupyter guidelines, specifying dockerhub tag rather than using "latest"
FROM jupyter/datascience-notebook:c54800018c2c

# pip install jupyter kernel gateway
RUN pip install jupyter_kernel_gateway

# Make port 8888 available to the world outside this container
EXPOSE 8888

# run jupyter with kernel gateway when container launches
CMD ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--KernelGatewayApp.port=8888"]
