import heapq,os

class TreeNode():
	def __init__(self,value,freq):
		self.value = value
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self,other):
		return self.freq < other.freq

	def __eq__(self,other):
		return self.freq == other.freq

class HuffmanCoding():
	def __init__(self,path):
		self.path = path  
		self.__heap = []
		self.__codes = {}
		self.__reverse_codes = {}

	def __make_freq_dict(self,text):
		freq_dict = {}
		for char in text:
			if char not in freq_dict:
				freq_dict[char] = 0
			freq_dict[char]+=1
		return freq_dict

	def __build_heap(self,freq_dict):

		for char in freq_dict:
			node = TreeNode(char,freq_dict[char])
			heapq.heappush(self.__heap,node)

	def __build_tree(self):
		while len(self.__heap)>1:
			node1 = heapq.heappop(self.__heap)
			node2 = heapq.heappop(self.__heap)
			freq_sum = node1.freq+node2.freq
			new = TreeNode(None,freq_sum)
			new.left = node1
			new.right = node2
			heapq.heappush(self.__heap,new)
		return

	def __build_codes_helper(self,root,code):
		if root is None:
			return
		if root.value:
			self.__codes[root.value] = code
			self.__reverse_codes[code] = root.value
			return
		self.__build_codes_helper(root.left,code+"0")
		self.__build_codes_helper(root.right,code+"1")

	def __build_codes(self):
		root = heapq.heappop(self.__heap)
		self.__build_codes_helper(root,"")

	def __get_encoded_text(self,text):
		encoded_text = ""
		for char in text:
			encoded_text += self.__codes[char]
		return encoded_text

	def __get_padded_encoded_text(self,encoded_text):
		padded_len = 8 - (len(encoded_text)%8)
		for i in range(padded_len):
			encoded_text += "0"
		padded_encoded_text = '{0:08b}'.format(padded_len) + encoded_text
		return padded_encoded_text

	def __get_bytes_array(self,padded_encoded_text):
		bytes_array = []

		for i in range(0,len(padded_encoded_text),8):
			byte = padded_encoded_text[i:i+8]
			bytes_array.append(int(byte,2))
		return bytes_array


	def compress(self):
		# get file from path and read it
		file_name,file_ext = os.path.splitext(self.path)
		output_path = file_name +"_compressed" + ".bin"
		with open(self.path,'r+') as file, open(output_path,'wb') as output:
			input_text = file.read()
			input_text = input_text.rstrip()
			# make frequency dictionary using the text
			freq_dict = self.__make_freq_dict(input_text)
			# construct min-heap from the frequency dictionary
			self.__build_heap(freq_dict)
			# construct binary tree from the heap
			self.__build_tree()
			# construct codes from binary tree
			self.__build_codes()
			# create the encoded text using the codes
			encoded_text = self.__get_encoded_text(input_text)
			# pad the encoded text
			padded_encoded_text = self.__get_padded_encoded_text(encoded_text)
			# get bytes array from padded encoded text
			bytes_array = self.__get_bytes_array(padded_encoded_text)
			# put this encoded text in the binary file
			final_bytes = bytes(bytes_array)
			# return binary file as output
			output.write(final_bytes)
		print("Compression Successful!")
		return output_path

	def __remove_padding(self,text):
		padding_info = text[:8]
		extra_padding = int(padding_info,2)
		text = text[8:]
		text_after_padding_removed = text[:-1*extra_padding]
		return text_after_padding_removed

	def __decode_text(self,text):
		decompressed_text = ""
		current_bits = ""

		for bit in text:
			current_bits += bit
			if current_bits in self.__reverse_codes:
				char = self.__reverse_codes[current_bits]
				decompressed_text += char
				current_bits = ""
		return decompressed_text

	def decompress(self,input_path):
		file_name,file_ext = os.path.splitext(input_path)
		output_path = file_name[:-11] + "_decompressd" + ".txt"
		with open(input_path,'rb') as file, open(output_path,'w') as output:
			bit_string = ''
			# to read each byte one by one
			byte = file.read(1)
			while byte:
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8,'0')
				bit_string += bits
				byte = file.read(1)
			actual_text = self.__remove_padding(bit_string)
			decompressed_text = self.__decode_text(actual_text)
			output.write(decompressed_text)
		print("Decompression Successful!")
		return
if __name__ == '__main__':
	path = input("Enter complete path of the text file: \n")
	h = HuffmanCoding(path)
	output_path = h.compress()
	x = input("Do you want to decompress? Y/N\n")
	if x =="Y":
		h.decompress(output_path)
	else:
		pass

		
		