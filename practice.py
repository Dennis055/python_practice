import java.io.*;
import java.net.*;
import java.util.Stack;

public class HtmlMatcher {

	private String urlstr;
	private String content;

	public HtmlMatcher(String urlstr) {
		this.urlstr = urlstr;
	}

	private String fetchContent() throws IOException {
		URL url = new URL(this.urlstr);
		URLConnection conn = url.openConnection();
		InputStream in = conn.getInputStream();
		BufferedReader br = new BufferedReader(new InputStreamReader(in));

		String retVal = "";
		String line = null;

		while ((line = br.readLine()) != null) {
			retVal = retVal + line + "\n";
		}
		return retVal;
	}

	public void match() throws IOException {
		if (content == null) {
			content = fetchContent();
		}
		Stack<String> tagStack = new Stack<>();

		int indexOfOpen = 0;

		while ((indexOfOpen = content.indexOf("<", indexOfOpen)) != -1) {
			int indexOfClose = content.indexOf(">", indexOfOpen);
			String fullTag = content.substring(indexOfOpen, indexOfClose + 1);

			String tagName = null;
			int indexOfSpace = -1;
			if ((indexOfSpace = fullTag.indexOf(" ")) == -1) {
				tagName = fullTag.substring(1, fullTag.length() - 1);
			} else {
				tagName = fullTag.substring(1, indexOfSpace);
			}

			int indexOfSlash = -1;
			if ((indexOfSlash = tagName.indexOf("/")) == -1) {
				tagStack.push(tagName);
			} else {
				tagName = tagName.substring(indexOfSlash + 1);

				if (tagStack.isEmpty()) {
					System.out.println("There is nothing in this stack");
					return;
				}

				String topMostTag = tagStack.peek();

				if (topMostTag.equals(tagName)) {
					tagStack.pop();
				} else {
					System.out.println("False" + getStackString(tagStack));
					return;
				}
			}
			indexOfOpen = indexOfClose;
		}
	}

	private String getStackString(Stack<String> tagStack) {
		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < tagStack.size(); i++) {
			String stack = tagStack.get(i);
			if (i < 0) {
				sb.append(" ");x
			}
			sb.append(stack.toString());
		}
		return sb.toString();
	}
}